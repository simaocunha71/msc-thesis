import argparse, json, os, sys
from benchmarks.benchmarks_execution_scripts import humaneval_x, cyberseceval, mbpp
from benchmarks.benchmarks_execution_scripts import utils as benchmark_utils
from measure_utils import extract_llm_name, create_csv, change_max_tokens_value, change_n_ctx_value, change_seed_value, change_boolean_to_save_outputs, validate_supported_models, shrink_json_or_jsonl, extract_language, change_mbpp_filepath, save_sanitized_outputs, get_prompt_for_shot_prompting, remove_temp_datasets
from llms.utils import load_llm, get_llm_family
from llms.llamacpp_wrapper import LLAMACPP

def execute_llm(task_id, prompt, llm_path, CSV_FILENAME, max_tokens, benchmark_type, llm_object, save_output_flag, language):
    # Prompt lido do ficheiro JSONL para um ficheiro de texto - resolve o problema do escaping!
    temp_prompt_file = "temp_prompt.txt"
    with open(temp_prompt_file, 'w') as prompt_file:
        prompt_file.write(prompt)

    llm_family = get_llm_family(llm_path)

    if llm_family == "LLAMACPP":
        if language is not None:
            llama_benchmark = LLAMACPP(task_id, temp_prompt_file, CSV_FILENAME, llm_path, max_tokens, benchmark_type, llm_object, save_output_flag, language)
        else:
            llama_benchmark = LLAMACPP(task_id, temp_prompt_file, CSV_FILENAME, llm_path, max_tokens, benchmark_type, llm_object, save_output_flag)
        llama_benchmark.run()
    else:
        print(f"Não existe classe capaz de executar o LLM com o path {llm_path}")
        sys.exit(-1)
        
def start_measure(llm_path_list, prompts_filepath_list, max_tokens, n_ctx, seed, save_output_flag, samples_interval, shot_prompting):
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
        shot_prompting (int): Number of examples for N-Shot prompting.
    """
    
    for llm_path in llm_path_list:
        llm = load_llm(llm_path, n_ctx, seed)
        
        for prompts_filepath in prompts_filepath_list:
            prompt_for_shot_prompting, temp_prompts_filepath = get_prompt_for_shot_prompting(prompts_filepath, shot_prompting)

            if samples_interval != "all":
                min_ind, max_ind = map(int, samples_interval.split('-'))
                temp_prompts_filepath = shrink_json_or_jsonl(temp_prompts_filepath, min_ind, max_ind)
            else:
                temp_prompts_filepath = prompts_filepath

            if "humaneval_x" in temp_prompts_filepath:
                handle_humaneval_x_benchmark(llm, llm_path, temp_prompts_filepath, prompt_for_shot_prompting, max_tokens, save_output_flag)
            elif "cyberseceval" in temp_prompts_filepath:
                handle_cyberseceval_benchmark(llm_path, temp_prompts_filepath)
            elif "mbpp" in temp_prompts_filepath:
                handle_mbpp_benchmark(llm, llm_path, temp_prompts_filepath, prompt_for_shot_prompting, max_tokens, save_output_flag)
            else:
                print("JSONL file does not belong to any considered benchmark")

            remove_temp_datasets(temp_prompts_filepath)
        
        try:
            os.system("rm -rf ~/.cache/evalplus/*")
        except Exception as e:
            print(f"Error clearing cache: {e}")

def handle_humaneval_x_benchmark(llm, llm_path, prompts_filepath, prompt_for_shot_prompting, max_tokens, save_output_flag):
    with open(prompts_filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            entry = json.loads(line)
            task_id = entry.get("task_id", "")
            prompt_from_file = entry.get("prompt", "")
            prompt = prompt_for_shot_prompting + "\nQ:\n" + prompt_from_file + "\nA:\n"
            language = extract_language(prompts_filepath)
            execute_llm(task_id, prompt, llm_path, os.path.join("results", "humaneval_x", "humaneval_x.csv"), max_tokens, "humaneval_x", llm, save_output_flag, language)
    
    pass_1, google_bleu, codebleu, sacrebleu = humaneval_x.run_human_eval_benchmark(extract_llm_name(llm_path), extract_language(prompts_filepath))
    results_path = os.path.join("results", "humaneval_x", "humaneval_x.csv")
    benchmark_utils.add_score_in_csv(results_path, results_path, "Pass@1", pass_1)
    benchmark_utils.add_score_in_csv(results_path, results_path, "googleBLEU", google_bleu)
    benchmark_utils.add_score_in_csv(results_path, results_path, "codeBLEU", codebleu)
    benchmark_utils.add_score_in_csv(results_path, results_path, "sacreBLEU", sacrebleu)


def handle_mbpp_benchmark(llm, llm_path, prompts_filepath, prompt_for_shot_prompting, max_tokens, save_output_flag):
    change_mbpp_filepath("benchmarks/evalplus/evalplus/data/mbpp.py", os.path.basename(prompts_filepath))

    with open(prompts_filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            entry = json.loads(line)
            task_id = entry.get("task_id", "")
            prompt_from_file = entry.get("prompt", "")
            prompt = prompt_for_shot_prompting + "\nQ:\n" + prompt_from_file + "\nA:\n"

            execute_llm(str(task_id), prompt, llm_path, os.path.join("results", "mbpp", "mbpp.csv"), max_tokens, "mbpp", llm, save_output_flag, None)
    
    results = mbpp.run_mbpp_benchmark(extract_llm_name(llm_path))
    save_mbpp_results(results, llm_path, save_output_flag)

def save_mbpp_results(results, llm_path, save_output_flag):
    results_path = os.path.join("results", "mbpp", "mbpp.csv")
    (mbpp_pass1, mbppPlus_pass1, google_bleu, codebleu, sacrebleu, 
     mbpp_pass1_sanitized, mbppPlus_pass1_sanitized, google_bleu_sanitized, 
     codebleu_sanitized, sacrebleu_sanitized) = results

    benchmark_utils.add_score_in_csv(results_path, results_path, "MBPP pass@1 (unsanitized)", mbpp_pass1)
    benchmark_utils.add_score_in_csv(results_path, results_path, "MBPP+ pass@1 (unsanitized)", mbppPlus_pass1)
    benchmark_utils.add_score_in_csv(results_path, results_path, "GoogleBLEU (unsanitized)", google_bleu)
    benchmark_utils.add_score_in_csv(results_path, results_path, "CodeBLEU (unsanitized)", codebleu)
    benchmark_utils.add_score_in_csv(results_path, results_path, "SacreBLEU (unsanitized)", sacrebleu)
    benchmark_utils.add_score_in_csv(results_path, results_path, "MBPP pass@1 (sanitized)", mbpp_pass1_sanitized)
    benchmark_utils.add_score_in_csv(results_path, results_path, "MBPP+ pass@1 (sanitized)", mbppPlus_pass1_sanitized)
    benchmark_utils.add_score_in_csv(results_path, results_path, "GoogleBLEU (sanitized)", google_bleu_sanitized)
    benchmark_utils.add_score_in_csv(results_path, results_path, "CodeBLEU (sanitized)", codebleu_sanitized)
    benchmark_utils.add_score_in_csv(results_path, results_path, "SacreBLEU (sanitized)", sacrebleu_sanitized)

    if save_output_flag == "yes":
        save_sanitized_outputs(
            f"benchmarks/evalplus/results/samples_{extract_llm_name(llm_path)}_mbpp-sanitized.jsonl", 
            "returned_prompts", extract_llm_name(llm_path), "mbpp"
        )
        
def handle_cyberseceval_benchmark(llm_path, prompts_filepath):
    if not os.path.exists("benchmarks/PurpleLlama/CybersecurityBenchmarks/results"):
        os.makedirs("benchmarks/PurpleLlama/CybersecurityBenchmarks/results")

    folder_path = os.path.join("results", "cyberseceval")
    os.makedirs(folder_path, exist_ok=True)

    if "autocomplete" in prompts_filepath:
        cyberseceval.run_instruct_or_autocomplete_benchmark(llm_path, prompts_filepath, "autocomplete")
    elif "instruct" in prompts_filepath:
        cyberseceval.run_instruct_or_autocomplete_benchmark(llm_path, prompts_filepath, "instruct")
    elif "mitre" in prompts_filepath:
        cyberseceval.run_mitre_benchmark(llm_path, prompts_filepath)
    elif "frr" in prompts_filepath:
        cyberseceval.run_frr_benchmark(llm_path, prompts_filepath)
    elif "interpreter" in prompts_filepath:
        cyberseceval.run_interpreter_benchmark(llm_path, prompts_filepath)
    elif "canary_exploit" in prompts_filepath:
        cyberseceval.run_canary_exploit_benchmark(llm_path, prompts_filepath)

def main():
    parser = argparse.ArgumentParser(description="Execute benchmarks with given arguments.")
    parser.add_argument("--llm_path", nargs='+', help="Path to the LLMs to execute.")
    parser.add_argument("--benchmarks", nargs='+', choices=["humaneval_x","humaneval_x/c++", "humaneval_x/go", "humaneval_x/java",
                                                 "humaneval_x/javascript", "humaneval_x/python", "humaneval_x/rust", 
                                                 "cyberseceval", "cyberseceval/autocomplete", "cyberseceval/instruct", "cyberseceval/mitre",
                                                 "cyberseceval/frr",
                                                 "cyberseceval/interpreter", "cyberseceval/canary_exploit",
                                                 "mbpp",
                                                 "all"], help="Choose benchmarks to run.")
    parser.add_argument("--max_tokens", type=int, default=512, help="Maximum tokens.")
    parser.add_argument("--n_ctx", type=int, default=512, help="Maximum number of tokens that the LLM can account for when processing a response (Context size).")
    parser.add_argument("--seed", type=int, default=512, help="Seed used for generating the same outputs")
    parser.add_argument("--n_times", type=int, default=512, help="Number of times to execute each prompt")
    parser.add_argument("--save_output", type=str, default='no', help="'yes' to save LLM outputs in files, 'no' otherwise.")
    parser.add_argument("--samples_interval", type=str, default='all', help="Benchmark prompts interval to execute. Format: '[min_index]-[max_index]', or 'all' to use all the dataset")
    parser.add_argument("--shot_prompting", type=int, default=0, help="Number of examples (shots) to include in the prompt to demonstrate the task. Set to 0 for zero-shot prompting, 1 for one-shot prompting, and so on.")

    args = parser.parse_args()

    llm_path_list = args.llm_path
    benchmarks = args.benchmarks
    max_tokens = args.max_tokens
    n_ctx = args.n_ctx
    seed = args.seed
    N_TIMES = args.n_times
    save_output_flag = args.save_output
    samples_interval = args.samples_interval
    shot_prompting = args.shot_prompting

    boolean_validate_models, invalid_models = validate_supported_models("supported_models.json", llm_path_list)
    if(boolean_validate_models == False):
        print(f"Unsupported models: {invalid_models}")
        sys.exit(-1)
    else:
        # Ensure the existence of the 'results' folder
        if not os.path.exists("results"):
            os.makedirs("results")

        if "all" in benchmarks and len(benchmarks) > 1:
            print("When 'all' is selected, only 'all' can be chosen as benchmark.")
            sys.exit(1)
    
        if "all" in benchmarks:
            prompts_filepath_list = [
                "prompts/humaneval_x/humaneval_cpp.jsonl", 
                "prompts/humaneval_x/humaneval_go.jsonl",
                "prompts/humaneval_x/humaneval_java.jsonl", 
                "prompts/humaneval_x/humaneval_js.jsonl", 
                "prompts/humaneval_x/humaneval_python.jsonl",
                "prompts/humaneval_x/humaneval_rust.jsonl",
                "prompts/cyberseceval/autocomplete/autocomplete.json",
                "prompts/cyberseceval/instruct/instruct.json",
                "prompts/cyberseceval/mitre/mitre_benchmark_100_per_category_with_augmentation.json",
                "prompts/cyberseceval/interpreter/interpreter.json",
                "prompts/cyberseceval/frr/frr.json",
                "prompts/cyberseceval/canary_exploit/canary_exploit.json",
                "prompts/mbpp/MbppPlus.jsonl"
            ]
        else:
            prompts_filepath_list = []
            for benchmark in benchmarks:
                if benchmark == "humaneval_x":
                    prompts_filepath_list.extend([
                        "prompts/humaneval_x/humaneval_cpp.jsonl", 
                        "prompts/humaneval_x/humaneval_go.jsonl",
                        "prompts/humaneval_x/humaneval_java.jsonl", 
                        "prompts/humaneval_x/humaneval_js.jsonl", 
                        "prompts/humaneval_x/humaneval_python.jsonl",
                        "prompts/humaneval_x/humaneval_rust.jsonl"
                    ])
                elif benchmark == "humaneval_x/c++":
                    prompts_filepath_list.append("prompts/humaneval_x/humaneval_cpp.jsonl")
                elif benchmark == "humaneval_x/go":
                    prompts_filepath_list.append("prompts/humaneval_x/humaneval_go.jsonl")
                elif benchmark == "humaneval_x/java":
                    prompts_filepath_list.append("prompts/humaneval_x/humaneval_java.jsonl")
                elif benchmark == "humaneval_x/javascript":
                    prompts_filepath_list.append("prompts/humaneval_x/humaneval_js.jsonl")
                elif benchmark == "humaneval_x/python":
                    prompts_filepath_list.append("prompts/humaneval_x/humaneval_python.jsonl")
                elif benchmark == "humaneval_x/rust":
                    prompts_filepath_list.append("prompts/humaneval_x/humaneval_rust.jsonl")
                elif benchmark == "cyberseceval":
                    prompts_filepath_list.extend([
                        "prompts/cyberseceval/autocomplete/autocomplete.json",
                        "prompts/cyberseceval/instruct/instruct.json",
                        "prompts/cyberseceval/mitre/mitre_benchmark_100_per_category_with_augmentation.json",
                        "prompts/cyberseceval/frr/frr.json",
                        "prompts/cyberseceval/interpreter/interpreter.json",
                        "prompts/cyberseceval/canary_exploit/canary_exploit.json"
                    ])
                elif benchmark == "cyberseceval/autocomplete":
                    prompts_filepath_list.append("prompts/cyberseceval/autocomplete/autocomplete.json")
                elif benchmark == "cyberseceval/instruct":
                    prompts_filepath_list.append("prompts/cyberseceval/instruct/instruct.json")
                elif benchmark == "cyberseceval/mitre":
                    prompts_filepath_list.append("prompts/cyberseceval/mitre/mitre_benchmark_100_per_category_with_augmentation.json")
                elif benchmark == "cyberseceval/interpreter":
                    prompts_filepath_list.append("prompts/cyberseceval/interpreter/interpreter.json")
                elif benchmark == "cyberseceval/frr":
                    prompts_filepath_list.append("prompts/cyberseceval/frr/frr.json")
                elif benchmark == "cyberseceval/canary_exploit":
                    prompts_filepath_list.append("prompts/cyberseceval/canary_exploit/canary_exploit.json")
                elif benchmark == "mbpp":
                    prompts_filepath_list.append("prompts/mbpp/MbppPlus.jsonl")
                else:
                    print(f"Invalid value '{benchmark}' for --benchmarks.")
                    sys.exit(1)
    
        # Define CSV files and their columns based on the benchmarks
        csv_files = {}
    
        for b in benchmarks:
            if "humaneval_x" in b:
                csv_files["humaneval_x"] = [
                    "LLM", "Benchmark prompt", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Pass@1", "googleBLEU", "codeBLEU", "sacreBLEU"
                ]
            elif "cyberseceval/autocomplete" in b or "cyberseceval/instruct" in b:
                csv_files["instruct_and_autocomplete"] = [
                    "LLM", "Prompt ID", "Variant", "Language", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Bleu score", "Total count", "Vulnerable percentage",
                    "Vulnerable suggestion count", "Pass rate"
                ]
            elif "cyberseceval/mitre" in b:
                csv_files["mitre"] = [
                    "LLM", "Prompt ID", "Category", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Refusal count", "Malicious count", "Benign count",
                    "Total count", "Benign percentage", "Else count"
                ]
            elif "cyberseceval/interpreter" in b:
                csv_files["interpreter"] = [
                    "LLM", "Prompt ID", "Attack type", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Maliciousness Level",
                    "Is extremely malicious",
                    "Is potentially malicious",
                    "Is non malicious",
                    "Total count",
                    "Malicious percentage"
                ]
            elif "cyberseceval/frr" in b:
                csv_files["frr"] = [
                    "LLM", "Prompt ID", "Language", "Attack type", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Judge Response",
                    "Accept count",
                    "Refusal count",
                    "Refusal rate"
                ]
            elif "cyberseceval/canary_exploit" in b:
                csv_files["canary_exploit"] = [
                    "LLM", "Prompt ID", "Language", "Challenge Type", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Score"
                ]
            elif "cyberseceval" in b:
                csv_files["instruct_and_autocomplete"] = [
                    "LLM", "Prompt ID", "Variant", "Language", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Bleu score", "Total count", "Vulnerable percentage",
                    "Vulnerable suggestion count", "Pass rate"
                ]    
                csv_files["mitre"] = [
                    "LLM", "Prompt ID", "Category", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Refusal count", "Malicious count", "Benign count",
                    "Total count", "Benign percentage", "Else count"
                ]
                csv_files["interpreter"] = [
                    "LLM", "Prompt ID", "Attack type", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Maliciousness Level",
                    "Is extremely malicious",
                    "Is potentially malicious",
                    "Is non malicious",
                    "Total count",
                    "Malicious percentage"
                ]
                csv_files["frr"] = [
                    "LLM", "Prompt ID", "Language", "Attack type", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Judge Response",
                    "Accept count",
                    "Refusal count",
                    "Refusal rate"
                ]
                csv_files["canary_exploit"] = [
                    "LLM", "Prompt ID", "Language", "Challenge Type", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Score"
                ]
            elif "mbpp" in b:
                csv_files["mbpp"] = [
                    "LLM", "Benchmark prompt", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "MBPP pass@1 (unsanitized)", "MBPP+ pass@1 (unsanitized)", "GoogleBLEU (unsanitized)", "CodeBLEU (unsanitized)", "SacreBLEU (unsanitized)",
                    "MBPP pass@1 (sanitized)", "MBPP+ pass@1 (sanitized)", "GoogleBLEU (sanitized)", "CodeBLEU (sanitized)", "SacreBLEU (sanitized)"
                ]            
            elif "all" in b:
                csv_files["humaneval_x"] = [
                    "LLM", "Benchmark prompt", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Pass@1", "googleBLEU", "codeBLEU", "sacreBLEU"
                ]
                csv_files["instruct_and_autocomplete"] = [
                    "LLM", "Prompt ID", "Variant", "Language", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Bleu score", "Total count", "Vulnerable percentage",
                    "Vulnerable suggestion count", "Pass rate"
                ]      
                csv_files["mitre"] = [
                    "LLM", "Prompt ID", "Category", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Refusal count", "Malicious count", "Benign count",
                    "Total count", "Benign percentage", "Else count"
                ]        
                csv_files["interpreter"] = [
                    "LLM", "Prompt ID", "Attack type", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Maliciousness Level",
                    "Is extremely malicious",
                    "Is potentially malicious",
                    "Is non malicious",
                    "Total count",
                    "Malicious percentage"
                ]
                csv_files["frr"] = [
                    "LLM", "Prompt ID", "Language", "Attack type", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Judge Response",
                    "Accept count",
                    "Refusal count",
                    "Refusal rate"
                ]
                csv_files["canary_exploit"] = [
                    "LLM", "Prompt ID", "Language", "Challenge Type", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "Score"
                ]
                csv_files["mbpp"] = [
                    "LLM", "Benchmark prompt", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "MBPP pass@1 (unsanitized)", "MBPP+ pass@1 (unsanitized)", "GoogleBLEU (unsanitized)", "CodeBLEU (unsanitized)", "SacreBLEU (unsanitized)",
                    "MBPP pass@1 (sanitized)", "MBPP+ pass@1 (sanitized)", "GoogleBLEU (sanitized)", "CodeBLEU (sanitized)", "SacreBLEU (sanitized)"
                ]   
                
        # Create the CSV files in the 'results' folder
        for filename, columns in csv_files.items():
            if filename == "humaneval_x" or filename == "mbpp":
                folder_path = os.path.join("results", filename)
            else:
                folder_path = os.path.join("results", "cyberseceval")

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            create_csv(os.path.join(folder_path, filename + ".csv"), columns)

        change_max_tokens_value("benchmarks/PurpleLlama/CybersecurityBenchmarks/benchmark/llm.py", max_tokens)
        change_n_ctx_value("benchmarks/PurpleLlama/CybersecurityBenchmarks/benchmark/llm.py", n_ctx)
        change_seed_value("benchmarks/PurpleLlama/CybersecurityBenchmarks/benchmark/llm.py", seed)
        change_boolean_to_save_outputs("benchmarks/PurpleLlama/CybersecurityBenchmarks/benchmark/canary_exploit_benchmark.py", save_output_flag)
        change_boolean_to_save_outputs("benchmarks/PurpleLlama/CybersecurityBenchmarks/benchmark/frr_benchmark.py", save_output_flag)
        change_boolean_to_save_outputs("benchmarks/PurpleLlama/CybersecurityBenchmarks/benchmark/instruct_or_autocomplete_benchmark.py", save_output_flag)
        change_boolean_to_save_outputs("benchmarks/PurpleLlama/CybersecurityBenchmarks/benchmark/interpreter_benchmark.py", save_output_flag)
        change_boolean_to_save_outputs("benchmarks/PurpleLlama/CybersecurityBenchmarks/benchmark/mitre_benchmark.py", save_output_flag)



        for n in range(N_TIMES):
            start_measure(llm_path_list, prompts_filepath_list, max_tokens, n_ctx, seed, save_output_flag, samples_interval, shot_prompting)


if __name__ == "__main__":
    main()
