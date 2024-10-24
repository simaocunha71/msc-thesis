import argparse, json, os, sys
from benchmarks.benchmarks_execution_scripts import humaneval_x, cyberseceval, mbpp
from benchmarks.benchmarks_execution_scripts import utils as benchmark_utils
from llama_cpp import Llama
from measure_utils import extract_llm_name, create_csv, validate_supported_models, process_interval, extract_language, change_mbpp_filepath, save_sanitized_outputs, get_prompt_for_shot_prompting, get_prompt_for_shot_prompting_cyberseceval, remove_temp_datasets, sleep_between_executions
from llms.utils import load_llm, get_llm_family
from llms.llamacpp_wrapper import LLAMACPP
from csv_files_headers import set_csv_headers

def execute_llm(llm_obj: Llama, task_id: int, prompt: str, llm_path: str, 
                CSV_FILENAME: str, max_tokens: int, top_p: float, temperature: float, 
                benchmark_type: str, save_output_flag: str, language: str, 
                seed: int, output_counter_id: int, n_shot: int, pass_k: int) -> None:
    """
    Execute measurement scripts for all considered models.
    NOTE: The prompt is read from the JSONL file to a text file, which resolves the escaping problems 
    that occurred in previous versions of the project. However, in the current version (30 Sept 2024), 
    Python provides more efficient ways to read a prompt directly from the JSON file 
    instead of using the method implemented here.

    Args:
        llm_obj (Llama): Llama object with the model loaded.
        task_id (int): Prompt ID to execute.
        prompt (str): Prompt to execute.
        llm_path (str): LLM path.
        CSV_FILENAME (str): CSV to append the metrics.
        max_tokens (int): Max tokens used by the LLM to generate responses.
        top_p (float): The top-p value to use for nucleus sampling.
        temperature (float): The temperature to use for sampling.
        benchmark_type (str): Type of benchmark to execute - "MBPP" or "HumanEval-X"
        save_output_flag (str): Indicates if the results should be saved ('yes' or 'no').
        language (str): Language of the HumanEval-X. NOTE: it is None in MBPP.
        seed (int): Seed used for generating the same outputs.
        output_counter_id (int): ID of the generation when calculating pass@k.
        n_shot (int): Number of examples (shots) to include in the prompt to demonstrate the task.
        pass_k (int): Max number of k to evaluate in pass@k metric.
    """

    temp_prompt_file = "temp_prompt.txt"
    with open(temp_prompt_file, 'w') as prompt_file:
        prompt_file.write(prompt)

    llm_family = get_llm_family(llm_path)

    if llm_family == "LLAMACPP":
        if language is not None:
            llama_benchmark = LLAMACPP(llm_obj, task_id, temp_prompt_file, CSV_FILENAME, llm_path, seed, max_tokens, top_p, temperature, benchmark_type, save_output_flag, output_counter_id, str(n_shot), str(pass_k), language)
        else:
            llama_benchmark = LLAMACPP(llm_obj, task_id, temp_prompt_file, CSV_FILENAME, llm_path, seed, max_tokens, top_p, temperature, benchmark_type, save_output_flag, output_counter_id, str(n_shot), str(pass_k))
        llama_benchmark.run()
    else:
        print(f"Não existe classe capaz de executar o LLM com o path {llm_path}")
        sys.exit(-1)
        
def start_measure(llm_path_list: list, prompts_filepath_list: list, max_tokens: int, n_ctx: int, 
                  seed: int, save_output_flag: str, samples_interval: str, shot_prompting: int, 
                  SLEEP_TIME: float, pass_k: int, top_p: float, temperature: float) -> None:
    """
    Execute measurement scripts for all considered models.

    Args:
        llm_path_list (list): List of paths to the LLMs.
        prompts_filepath_list (list): List of paths to the prompt files.
        max_tokens (int): Maximum number of tokens.
        n_ctx (int): Context size (maximum tokens the LLM can process).
        seed (int): Seed for generating reproducible results.
        save_output_flag (str): Indicates if the results should be saved ('yes' or 'no').
        samples_interval (str): Sample interval to execute. Format: '[min_index]-[max_index]', or 'all' to use the entire dataset.
        shot_prompting (int): Number of examples for N-shot prompting.
        SLEEP_TIME (float): Sleep time between executions.
        pass_k: Max number of k to evaluate in pass@k metric: 1, 10 or 100 (currently supported)
        top_p (float): The top-p value to use for nucleus sampling.
        temperature (float): The temperature to use for sampling
    """

    def handle_prompt_files(llm_obj, llm_path, prompts_filepath, pass_k):
        prompt_for_shot_prompting, temp_prompts_filepath = get_prompt_for_shot_prompting(prompts_filepath, shot_prompting)
        temp_prompts_filepath = process_interval(temp_prompts_filepath, samples_interval)

        if "humaneval_x" in temp_prompts_filepath:
            handle_humaneval_x_benchmark(llm_obj, llm_path, temp_prompts_filepath, prompt_for_shot_prompting, max_tokens, top_p, temperature, save_output_flag, SLEEP_TIME, shot_prompting, pass_k, seed)
        elif "mbpp" in temp_prompts_filepath:
            handle_mbpp_benchmark(llm_obj, llm_path, temp_prompts_filepath, prompt_for_shot_prompting, max_tokens, top_p, temperature, save_output_flag, SLEEP_TIME, shot_prompting, pass_k, seed)
        else:
            print("JSONL file does not belong to any considered benchmark")

        remove_temp_datasets(temp_prompts_filepath)

    for llm_path in llm_path_list:
        for prompts_filepath in prompts_filepath_list:
            llm_obj = load_llm(llm_path, n_ctx, seed)
            
            handle_prompt_files(llm_obj, llm_path, prompts_filepath, pass_k)
        
        try:
            os.system("rm -rf ~/.cache/evalplus/*")
        except Exception as e:
            print(f"Error clearing cache: {e}")

def handle_humaneval_x_benchmark(llm_obj: Llama, llm_path: str, prompts_filepath: str, 
                                 prompt_for_shot_prompting: str, max_tokens: int, top_p: float, 
                                 temperature: float, save_output_flag: str, 
                                 SLEEP_TIME: float, shot_prompting: int, pass_k: int, seed: int):
    """
    Read the dataset from HumanEval-X from a certain language (obtained in `prompts_filepath`) line by line and execute the LLM with the prompt.
    Args:
        llm_obj (Llama): Llama object with the model loaded.
        llm_path (str): LLM path.
        prompts_filepath (str): Dataset path.
        prompt_for_shot_prompting_file (str): Text file containing the initial prompt for shot-prompting.
        max_tokens (int): Max tokens used by the LLM to generate responses.
        top_p (float): The top-p value to use for nucleus sampling.
        seed (int): Seed used for generating the same outputs.
        temperature (float): The temperature to use for sampling.
        save_output_flag (str): Indicates if the results should be saved ('yes' or 'no').
        SLEEP_TIME (float): Number of seconds to wait between executions.
        shot_prompting (int): Number of examples (shots) to include in the prompt to demonstrate the task.
        pass_k (int): Max number of k to evaluate in pass@k metric.
        n_shot (int): Number of examples (shots) to include in the prompt to demonstrate the task.
        seed (int): Seed used for generating the same outputs.
    """    
    list_of_seeds = [seed + i for i in range(pass_k)]
    
    with open(prompts_filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            entry = json.loads(line)
            task_id = entry.get("task_id", "")
            prompt_from_file = entry.get("prompt", "")
            prompt = prompt_for_shot_prompting + "\nQ:\n" + prompt_from_file + "\nA:\n"
            language = extract_language(prompts_filepath)
            for idx, sd in enumerate(list_of_seeds, start=1):
                execute_llm(llm_obj, task_id, prompt, llm_path, os.path.join("results", "humaneval_x", f"humaneval_x_{shot_prompting}_shot.csv"), max_tokens, top_p, temperature, "humaneval_x", save_output_flag, language, sd, idx, shot_prompting, pass_k)
            sleep_between_executions(secs=SLEEP_TIME)
    
    scores = humaneval_x.run_human_eval_benchmark(extract_llm_name(llm_path), extract_language(prompts_filepath), pass_k, shot_prompting)
    pass_1, pass_10, pass_100, google_bleu, codebleu, sacrebleu = scores["pass_1"], scores["pass_10"], scores["pass_100"], scores["google_bleu"], scores["codebleu"], scores["sacrebleu"]
    results_path = os.path.join("results", "humaneval_x", f"humaneval_x_{shot_prompting}_shot.csv")

    if pass_k not in [1,10,100]:
        print(f"[ERROR] pass@k value (k={pass_k}) not supported - only supported pass@1, pass@10 and pass@100")
        sys.exit(1)

    if pass_k == 1:
        benchmark_utils.add_score_in_csv(results_path, "Pass@1", pass_1)
    elif pass_k == 10:
        benchmark_utils.add_score_in_csv(results_path, "Pass@1", pass_1)
        benchmark_utils.add_score_in_csv(results_path, "Pass@10", pass_10)
    elif pass_k == 100:
        benchmark_utils.add_score_in_csv(results_path, "Pass@1", pass_1)
        benchmark_utils.add_score_in_csv(results_path, "Pass@10", pass_10)
        benchmark_utils.add_score_in_csv(results_path, "Pass@100", pass_100)

    benchmark_utils.add_score_in_csv(results_path, "GoogleBLEU", google_bleu)
    benchmark_utils.add_score_in_csv(results_path, "CodeBLEU", codebleu)
    benchmark_utils.add_score_in_csv(results_path, "SacreBLEU", sacrebleu)

def handle_mbpp_benchmark(llm_obj: Llama, llm_path: str, prompts_filepath: str, prompt_for_shot_prompting: str, 
                          max_tokens: int, top_p: float, temperature: float, save_output_flag: str, 
                          SLEEP_TIME: float, shot_prompting: int, pass_k: int, seed: int):
    """
    Read the dataset from MBPP (i.e., `MbppPlus.jsonl`) line by line and execute the LLM with the prompt.
    Args:
        llm_obj (Llama): Llama object with the model loaded.
        llm_path (str): LLM path.
        prompts_filepath (str): Dataset path.
        prompt_for_shot_prompting_file (str): Text file containing the initial prompt for shot-prompting.
        max_tokens (int): Max tokens used by the LLM to generate responses.
        top_p (float): The top-p value to use for nucleus sampling.
        seed (int): Seed used for generating the same outputs.
        temperature (float): The temperature to use for sampling.
        save_output_flag (str): Indicates if the results should be saved ('yes' or 'no').
        SLEEP_TIME (float): Number of seconds to wait between executions.
        shot_prompting (int): Number of examples (shots) to include in the prompt to demonstrate the task.
        pass_k (int): Max number of k to evaluate in pass@k metric.
        n_shot (int): Number of examples (shots) to include in the prompt to demonstrate the task.
        seed (int): Seed used for generating the same outputs.
    """

    change_mbpp_filepath("benchmarks/evalplus/evalplus/data/mbpp.py", os.path.basename(prompts_filepath))
    results_path = os.path.join("results", "mbpp", f"mbpp_{shot_prompting}_shot.csv")
    
    list_of_seeds = [seed + i for i in range(pass_k)]

    with open(prompts_filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            entry = json.loads(line)
            task_id = entry.get("task_id", "")
            prompt_from_file = entry.get("prompt", "")
            prompt = prompt_for_shot_prompting + "\nQ:\n" + prompt_from_file + "\nA:\n"

            for idx, sd in enumerate(list_of_seeds, start=1):
                execute_llm(llm_obj, str(task_id), prompt, llm_path, results_path, max_tokens, top_p, temperature, "mbpp", save_output_flag, None, sd, idx, shot_prompting, pass_k)
            sleep_between_executions(secs=SLEEP_TIME)
    
    results = mbpp.run_mbpp_benchmark(extract_llm_name(llm_path), pass_k, shot_prompting)
    save_mbpp_results(results, llm_path, save_output_flag, results_path, pass_k, shot_prompting)

def save_mbpp_results(results: tuple, llm_path: str, save_output_flag: str, 
                      results_path: str, pass_k: int, n_shot: int) -> None:
    """
    Add the pass@k and BLEU scores in the correct columns of the CSV
    Args:
        results (tuple): pass@k and BLEU scores.
        llm_path (str): LLM path.
        save_output_flag (str): Indicates if the results should be saved ('yes' or 'no').
        results_path (str): CSV path to save the results.
        pass_k (int): Max number of k to evaluate in pass@k metric.
        n_shot (int): Number of examples (shots) to include in the prompt to demonstrate the task.
    """

    (mbpp_unsan_pass_1, mbpp_san_pass_1, mbppPlus_unsan_pass_1, mbppPlus_san_pass_1, 
     mbpp_unsan_pass_10, mbpp_san_pass_10, mbppPlus_unsan_pass_10, mbppPlus_san_pass_10, 
     mbpp_unsan_pass_100, mbpp_san_pass_100, mbppPlus_unsan_pass_100, mbppPlus_san_pass_100,
     unsan_google_bleu, san_google_bleu, unsan_codebleu, san_codebleu, unsan_sacrebleu, san_sacrebleu) = results

    if pass_k not in [1,10,100]:
        print(f"[ERROR] pass@k value (k={pass_k}) not supported - only supported pass@1, pass@10 and pass@100")
        sys.exit(1)

    if pass_k == 1:
        benchmark_utils.add_score_in_csv(results_path, "MBPP (unsanitized) pass@1", mbpp_unsan_pass_1)
        benchmark_utils.add_score_in_csv(results_path, "MBPP+ (unsanitized) pass@1", mbppPlus_unsan_pass_1)
        benchmark_utils.add_score_in_csv(results_path, "GoogleBLEU (unsanitized)", unsan_google_bleu)
        benchmark_utils.add_score_in_csv(results_path, "CodeBLEU (unsanitized)", unsan_codebleu)
        benchmark_utils.add_score_in_csv(results_path, "SacreBLEU (unsanitized)", unsan_sacrebleu)

        benchmark_utils.add_score_in_csv(results_path, "MBPP (sanitized) pass@1", mbpp_san_pass_1)
        benchmark_utils.add_score_in_csv(results_path, "MBPP+ (sanitized) pass@1", mbppPlus_san_pass_1)
        benchmark_utils.add_score_in_csv(results_path, "GoogleBLEU (sanitized)", san_google_bleu)
        benchmark_utils.add_score_in_csv(results_path, "CodeBLEU (sanitized)", san_codebleu)
        benchmark_utils.add_score_in_csv(results_path, "SacreBLEU (sanitized)", san_sacrebleu)

    elif pass_k == 10:
        benchmark_utils.add_score_in_csv(results_path, "MBPP (unsanitized) pass@1", mbpp_unsan_pass_1)
        benchmark_utils.add_score_in_csv(results_path, "MBPP+ (unsanitized) pass@1", mbppPlus_unsan_pass_1)
        benchmark_utils.add_score_in_csv(results_path, "MBPP (unsanitized) pass@10", mbpp_unsan_pass_10)
        benchmark_utils.add_score_in_csv(results_path, "MBPP+ (unsanitized) pass@10", mbppPlus_unsan_pass_10)
        benchmark_utils.add_score_in_csv(results_path, "GoogleBLEU (unsanitized)", unsan_google_bleu)
        benchmark_utils.add_score_in_csv(results_path, "CodeBLEU (unsanitized)", unsan_codebleu)
        benchmark_utils.add_score_in_csv(results_path, "SacreBLEU (unsanitized)", unsan_sacrebleu)

        benchmark_utils.add_score_in_csv(results_path, "MBPP (sanitized) pass@1", mbpp_san_pass_1)
        benchmark_utils.add_score_in_csv(results_path, "MBPP+ (sanitized) pass@1", mbppPlus_san_pass_1)
        benchmark_utils.add_score_in_csv(results_path, "MBPP (sanitized) pass@10", mbpp_san_pass_10)
        benchmark_utils.add_score_in_csv(results_path, "MBPP+ (sanitized) pass@10", mbppPlus_san_pass_10)
        benchmark_utils.add_score_in_csv(results_path, "GoogleBLEU (sanitized)", san_google_bleu)
        benchmark_utils.add_score_in_csv(results_path, "CodeBLEU (sanitized)", san_codebleu)
        benchmark_utils.add_score_in_csv(results_path, "SacreBLEU (sanitized)", san_sacrebleu)

    elif pass_k == 100:
        benchmark_utils.add_score_in_csv(results_path, "MBPP (unsanitized) pass@1", mbpp_unsan_pass_1)
        benchmark_utils.add_score_in_csv(results_path, "MBPP+ (unsanitized) pass@1", mbppPlus_unsan_pass_1)
        benchmark_utils.add_score_in_csv(results_path, "MBPP (unsanitized) pass@10", mbpp_unsan_pass_10)
        benchmark_utils.add_score_in_csv(results_path, "MBPP+ (unsanitized) pass@10", mbppPlus_unsan_pass_10)
        benchmark_utils.add_score_in_csv(results_path, "MBPP (unsanitized) pass@100", mbpp_unsan_pass_100)
        benchmark_utils.add_score_in_csv(results_path, "MBPP+ (unsanitized) pass@100", mbppPlus_unsan_pass_100)
        benchmark_utils.add_score_in_csv(results_path, "GoogleBLEU (unsanitized)", unsan_google_bleu)
        benchmark_utils.add_score_in_csv(results_path, "CodeBLEU (unsanitized)", unsan_codebleu)
        benchmark_utils.add_score_in_csv(results_path, "SacreBLEU (unsanitized)", unsan_sacrebleu)

        benchmark_utils.add_score_in_csv(results_path, "MBPP (sanitized) pass@1", mbpp_san_pass_1)
        benchmark_utils.add_score_in_csv(results_path, "MBPP+ (sanitized) pass@1", mbppPlus_san_pass_1)
        benchmark_utils.add_score_in_csv(results_path, "MBPP (sanitized) pass@10", mbpp_san_pass_10)
        benchmark_utils.add_score_in_csv(results_path, "MBPP+ (sanitized) pass@10", mbppPlus_san_pass_10)
        benchmark_utils.add_score_in_csv(results_path, "MBPP (sanitized) pass@100", mbpp_san_pass_100)
        benchmark_utils.add_score_in_csv(results_path, "MBPP+ (sanitized) pass@100", mbppPlus_san_pass_100)
        benchmark_utils.add_score_in_csv(results_path, "GoogleBLEU (sanitized)", san_google_bleu)
        benchmark_utils.add_score_in_csv(results_path, "CodeBLEU (sanitized)", san_codebleu)
        benchmark_utils.add_score_in_csv(results_path, "SacreBLEU (sanitized)", san_sacrebleu)


    if save_output_flag == "yes":
        save_sanitized_outputs(
            f"benchmarks/evalplus/results/samples_{extract_llm_name(llm_path)}_mbpp_{n_shot}_shot-sanitized.jsonl", 
            "returned_prompts", extract_llm_name(llm_path), "mbpp", str(n_shot)
        )
        
def handle_cyberseceval_benchmark(llm_path: str, prompts_filepath: str, max_tokens: int, seed: int, 
                                  n_ctx: int, top_p: float, temperature: float, save_output_flag: str, 
                                  prompt_for_shot_prompting_file: str, SLEEP_TIME: float, 
                                  shot_prompting: int, n_times: int) -> None:
    """
    Redirects to the function of CyberSecEval called in the function.
    Args:
        llm_path (str): LLM path.
        prompts_filepath (str): Dataset path.
        max_tokens (int): Max tokens used by the LLM to generate responses.
        seed (int): Seed used for generating the same outputs.
        n_ctx (float): Context size.
        top_p (float): The top-p value to use for nucleus sampling.
        temperature (float): The temperature to use for sampling.
        save_output_flag (str): Indicates if the results should be saved ('yes' or 'no').
        prompt_for_shot_prompting_file (str): Text file containing the initial prompt for shot-prompting.
        SLEEP_TIME (float): Number of seconds to wait between executions.
        shot_prompting (int): Number of examples (shots) to include in the prompt to demonstrate the task.
        n_times (int): Number of times to execute the benchmark.
    """

    if not os.path.exists("benchmarks/PurpleLlama/CybersecurityBenchmarks/results"):
        os.makedirs("benchmarks/PurpleLlama/CybersecurityBenchmarks/results")

    folder_path = os.path.join("results", "cyberseceval")
    os.makedirs(folder_path, exist_ok=True)

    if "autocomplete" in prompts_filepath:
        cyberseceval.run_instruct_or_autocomplete_benchmark(llm_path, prompts_filepath, "autocomplete", max_tokens, seed, n_ctx, top_p, temperature, save_output_flag, prompt_for_shot_prompting_file, SLEEP_TIME, shot_prompting, n_times)
    elif "instruct" in prompts_filepath:
        cyberseceval.run_instruct_or_autocomplete_benchmark(llm_path, prompts_filepath, "instruct", max_tokens, seed, n_ctx, top_p, temperature, save_output_flag, prompt_for_shot_prompting_file, SLEEP_TIME, shot_prompting, n_times)
    elif "mitre" in prompts_filepath:
        cyberseceval.run_mitre_benchmark(llm_path, prompts_filepath, max_tokens, seed, n_ctx, top_p, temperature, save_output_flag, prompt_for_shot_prompting_file, SLEEP_TIME, shot_prompting, n_times)
    elif "frr" in prompts_filepath:
        cyberseceval.run_frr_benchmark(llm_path, prompts_filepath, max_tokens, seed, n_ctx, top_p, temperature, save_output_flag, prompt_for_shot_prompting_file, SLEEP_TIME, shot_prompting, n_times)
    elif "interpreter" in prompts_filepath:
        cyberseceval.run_interpreter_benchmark(llm_path, prompts_filepath,max_tokens, seed, n_ctx, top_p, temperature, save_output_flag, prompt_for_shot_prompting_file, SLEEP_TIME, shot_prompting, n_times)
    elif "canary_exploit" in prompts_filepath:
        cyberseceval.run_canary_exploit_benchmark(llm_path, prompts_filepath, max_tokens, seed, n_ctx, top_p, temperature, save_output_flag, prompt_for_shot_prompting_file, SLEEP_TIME, shot_prompting, n_times)


def main():
    parser = argparse.ArgumentParser(description="Execute benchmarks with given arguments.")
    parser.add_argument("--llm_path", nargs='+', required=True, help="Path to the LLMs to execute.")
    parser.add_argument("--benchmarks", nargs='+', choices=[
        "humaneval_x", "humaneval_x/c++", "humaneval_x/go", "humaneval_x/java",
        "humaneval_x/javascript", "humaneval_x/python", "humaneval_x/rust",
        "cyberseceval", "cyberseceval/autocomplete", "cyberseceval/instruct",
        "cyberseceval/mitre", "cyberseceval/frr", "cyberseceval/interpreter",
        "cyberseceval/canary_exploit", "mbpp"
    ], required=True, help="Choose benchmarks to run.")
    parser.add_argument("--max_tokens", type=int, default=512,
                        help="Max tokens used by the LLM to generate responses")
    parser.add_argument("--n_ctx", type=int, default=512,
                        help="Maximum number of tokens that the LLM can account for when processing a response (Context size).")
    parser.add_argument("--seed", type=int, default=512, help="Seed used for generating the same outputs")
    parser.add_argument("--n_times", type=int, default=1,
                        help="Number of times to execute each prompt")
    parser.add_argument("--save_output", type=str, choices=['yes', 'no'], default='no',
                        help="'yes' to save LLM outputs in files, 'no' otherwise.")
    parser.add_argument("--samples_interval", type=str, default='all',
                        help="Benchmark prompts interval to execute. Format: '[min_index]-[max_index]', or 'all' to use all the dataset")
    parser.add_argument("--n_shot_prompting", type=int, default=0,
                        help="Number of examples (shots) to include in the prompt to demonstrate the task. Set to 0 for zero-shot prompting, 1 for one-shot prompting, and so on.")
    parser.add_argument("--sleep_time", type=float, default=3.0,
                        help="Number of seconds to wait between executions.")
    parser.add_argument("--pass_k", type=int, default=1,
                        help="Max number of k to evaluate in pass@k metric: 1, 10 or 100 (currently supported)")
    parser.add_argument("--top_p", type=float, default=0.95,
                        help="The top-p value to use for nucleus sampling - default value is the same as in 'Purple Llama CyberSecEval: A benchmark for evaluating the cybersecurity risks of large language models'")
    parser.add_argument("--temperature", type=float, default=0.6,
                        help="The temperature to use for sampling -  default value is the same as in 'Purple Llama CyberSecEval: A benchmark for evaluating the cybersecurity risks of large language models'")

    args = parser.parse_args()

    llm_path_list = args.llm_path
    benchmarks = args.benchmarks
    max_tokens = args.max_tokens
    n_ctx = args.n_ctx
    seed = args.seed
    N_TIMES = args.n_times
    save_output_flag = args.save_output
    samples_interval = args.samples_interval
    shot_prompting = args.n_shot_prompting
    SLEEP_TIME = args.sleep_time
    pass_k = args.pass_k
    top_p = args.top_p
    temperature = args.temperature

    # Define benchmark groups
    humaneval_x_group = {
        "humaneval_x", "humaneval_x/c++", "humaneval_x/go", "humaneval_x/java",
        "humaneval_x/javascript", "humaneval_x/python", "humaneval_x/rust"
    }
    cyberseceval_group = {
        "cyberseceval", "cyberseceval/autocomplete", "cyberseceval/instruct",
        "cyberseceval/mitre", "cyberseceval/frr", "cyberseceval/interpreter",
        "cyberseceval/canary_exploit"
    }
    mbpp_group = {"mbpp"}

    selected_benchmarks = set(benchmarks)

    # Validate that selected benchmarks are from the same group
    if selected_benchmarks.issubset(humaneval_x_group):
        benchmark_group = "humaneval_x"
        print("Selected HumanEval-X benchmark")
    elif selected_benchmarks.issubset(cyberseceval_group):
        benchmark_group = "cyberseceval"
        print("Selected CyberSecEval benchmark")
    elif selected_benchmarks.issubset(mbpp_group):
        benchmark_group = "mbpp"
        print("Selected MBPP benchmark")
    else:
        print("[ERROR] You must select benchmarks from a single group (either HumanEval-X, CyberSecEval, or MBPP).")
        sys.exit(1)

    # Validate models
    boolean_validate_models, invalid_models = validate_supported_models("supported_models.json", llm_path_list)
    if not boolean_validate_models:
        print(f"[ERROR] Unsupported models: {invalid_models}")
        sys.exit(-1)
    else:
        # Ensure the existence of the 'results' folder
        if not os.path.exists("results"):
            os.makedirs("results")

        # Build prompts_filepath_list based on selected benchmarks
        prompts_filepath_list = []

        if benchmark_group == "humaneval_x":
            if "humaneval_x" in selected_benchmarks:
                prompts_filepath_list.extend([
                    "prompts/humaneval_x/humaneval_cpp.jsonl",
                    "prompts/humaneval_x/humaneval_go.jsonl",
                    "prompts/humaneval_x/humaneval_java.jsonl",
                    "prompts/humaneval_x/humaneval_js.jsonl",
                    "prompts/humaneval_x/humaneval_python.jsonl",
                ])
            else:
                for benchmark in selected_benchmarks:
                    if benchmark == "humaneval_x/c++":
                        prompts_filepath_list.append("prompts/humaneval_x/humaneval_cpp.jsonl")
                    elif benchmark == "humaneval_x/go":
                        prompts_filepath_list.append("prompts/humaneval_x/humaneval_go.jsonl")
                    elif benchmark == "humaneval_x/java":
                        prompts_filepath_list.append("prompts/humaneval_x/humaneval_java.jsonl")
                    elif benchmark == "humaneval_x/javascript":
                        prompts_filepath_list.append("prompts/humaneval_x/humaneval_js.jsonl")
                    elif benchmark == "humaneval_x/python":
                        prompts_filepath_list.append("prompts/humaneval_x/humaneval_python.jsonl")
                    else:
                        print(f"Invalid value '{benchmark}' for --benchmarks.")
                        sys.exit(1)
        elif benchmark_group == "cyberseceval":
            if "cyberseceval" in selected_benchmarks:
                prompts_filepath_list.extend([
                    "prompts/cyberseceval/autocomplete/autocomplete.json",
                    "prompts/cyberseceval/instruct/instruct.json",
                    "prompts/cyberseceval/mitre/mitre_benchmark_100_per_category_with_augmentation.json",
                    "prompts/cyberseceval/frr/frr.json",
                    "prompts/cyberseceval/interpreter/interpreter.json",
                    "prompts/cyberseceval/canary_exploit/canary_exploit.json"
                ])
            else:
                for benchmark in selected_benchmarks:
                    if benchmark == "cyberseceval/autocomplete":
                        prompts_filepath_list.append("prompts/cyberseceval/autocomplete/autocomplete.json")
                    elif benchmark == "cyberseceval/instruct":
                        prompts_filepath_list.append("prompts/cyberseceval/instruct/instruct.json")
                    elif benchmark == "cyberseceval/mitre":
                        prompts_filepath_list.append("prompts/cyberseceval/mitre/mitre_benchmark_100_per_category_with_augmentation.json")
                    elif benchmark == "cyberseceval/frr":
                        prompts_filepath_list.append("prompts/cyberseceval/frr/frr.json")
                    elif benchmark == "cyberseceval/interpreter":
                        prompts_filepath_list.append("prompts/cyberseceval/interpreter/interpreter.json")
                    elif benchmark == "cyberseceval/canary_exploit":
                        prompts_filepath_list.append("prompts/cyberseceval/canary_exploit/canary_exploit.json")
                    else:
                        print(f"Invalid value '{benchmark}' for --benchmarks.")
                        sys.exit(1)
        elif benchmark_group == "mbpp":
            prompts_filepath_list.append("prompts/mbpp/MbppPlus.jsonl")
        else:
            print("Invalid benchmark group.")
            sys.exit(1)

        # Define CSV files and their columns based on the benchmarks
        csv_files = set_csv_headers(list(selected_benchmarks), pass_k)

        # Create the CSV files in the 'results' folder
        for filename, columns in csv_files.items():
            if "humaneval_x" in filename:
                folder_path = os.path.join("results", "humaneval_x")
            elif "mbpp" in filename:
                folder_path = os.path.join("results", "mbpp")
            elif (
                "mitre" in filename or
                "interpreter" in filename or
                "frr" in filename or
                "instruct_and_autocomplete" in filename or
                "canary_exploit" in filename
            ):
                folder_path = os.path.join("results", "cyberseceval")
            else:
                folder_path = None

            if folder_path and not os.path.exists(folder_path):
                os.makedirs(folder_path)
            if ("mitre" in filename or "interpreter" in filename or "frr" in filename):
                create_csv(os.path.join(folder_path, filename + ".csv"), columns)
            else:
                create_csv(os.path.join(folder_path, filename + f"_{shot_prompting}_shot.csv"), columns)

        # Execution based on benchmark group
        if benchmark_group in ["humaneval_x", "mbpp"]:
            # MBPP or HumanEval-X execution
            for _ in range(N_TIMES):
                start_measure(llm_path_list, prompts_filepath_list, max_tokens, n_ctx, seed, save_output_flag,
                              samples_interval, shot_prompting, SLEEP_TIME, pass_k, top_p, temperature)
        else:
            # CyberSecEval execution
            for llm_path in llm_path_list:
                for prompts_filepath in prompts_filepath_list:
                    #prompt_for_shot_prompting, temp_prompts_filepath = get_prompt_for_shot_prompting_cyberseceval(prompts_filepath, shot_prompting, prompts_filepath.split("/")[2])
                    #TODO: Remover a linha 514 e descomentar 512, 528 e 529
                    temp_prompts_filepath = os.path.join(
                        os.path.dirname(prompts_filepath), 
                        f"{os.path.splitext(os.path.basename(prompts_filepath))[0]}_adapted{os.path.splitext(prompts_filepath)[1]}")
                    # Generate prompt for shot prompting and create a temporary prompts file
                    prompt_for_shot_prompting, _ = get_prompt_for_shot_prompting_cyberseceval(
                        prompts_filepath, shot_prompting, prompts_filepath.split("/")[2])
                    temp_prompts_filepath = process_interval(temp_prompts_filepath, samples_interval)
                    prompt_for_shot_prompting_file = "prompt_for_shot_prompting.txt"
                    with open(prompt_for_shot_prompting_file, 'w') as file:
                        file.write(prompt_for_shot_prompting)
                    handle_cyberseceval_benchmark(llm_path, temp_prompts_filepath, max_tokens, seed, n_ctx, top_p,
                                                  temperature, save_output_flag, prompt_for_shot_prompting_file,
                                                  SLEEP_TIME, shot_prompting, N_TIMES)
                    #os.remove(prompt_for_shot_prompting_file)
                    #remove_temp_datasets(temp_prompts_filepath)

if __name__ == "__main__":
    main()
