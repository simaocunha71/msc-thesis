import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import autocompleteOrInstruct_json_to_csv, mitre_json_to_csv, interpreter_json_to_csv, frr_json_to_csv, canary_exploit_json_to_csv

# Global definitions for LLMs
JUDGE_LLM = "LLAMACPP::llms/models/llama-2-7b.Q2_K_1.gguf::random_string"
EXPANSION_LLM = "LLAMACPP::llms/models/llama-2-7b.Q2_K_2.gguf::random_string"

def set_env_variables():
    """
    Set the necessary environment variables for the execution of the benchmark.

    This function sets the following environment variables:
    - WEGGLI_PATH: Specifies the path to the WEGGLI executable.
    - PATH: Updates the system PATH to include the Cargo bin directory for Rust tools.

    Environment Variables:
        WEGGLI_PATH (str): Path to the WEGGLI executable.
        PATH (str): Updated PATH variable including Cargo's bin directory.
    """
    
    # Set the path for WEGGLI - export WEGGLI_PATH=weggli
    os.environ['WEGGLI_PATH'] = 'weggli'
    
    # Update PATH to include Cargo's bin directory - export PATH="$HOME/.cargo/bin:$PATH"
    os.environ['PATH'] = f"{os.environ['HOME']}/.cargo/bin:{os.environ['PATH']}"


def run_instruct_or_autocomplete_benchmark(model: str, prompts_filepath: str, benchmark_type: str, 
                                           max_tokens: int, seed: int, n_ctx: int, top_p: float, temperature: float, 
                                           save_output_flag: str, prompt_for_shot_prompting_file: str, 
                                           SLEEP_TIME: float, shot_prompting: int, n_times: int):
    """
    Calculate the scores from the Instruct or Autocomplete benchmarks from CybersecEval.

    Args:
        model (str): LLM name.
        prompts_filepath (str): Dataset path.
        benchmark_type (str): Refers to "Autocomplete" or "Instruct"
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

    set_env_variables()
    model_short = os.path.splitext(os.path.basename(model))[0]

    command_to_execute_benchmark = f'python3 -m benchmarks.PurpleLlama.CybersecurityBenchmarks.benchmark.run ' \
        f'--benchmark={benchmark_type} ' \
        f'--max_tokens={max_tokens} ' \
        f'--seed={seed} ' \
        f'--n_ctx={n_ctx} ' \
        f'--top_p={top_p} ' \
        f'--temperature={temperature} ' \
        f'--save_output_flag={save_output_flag} ' \
        f'--sleep_time={SLEEP_TIME} ' \
        f'--n_shot_prompting={shot_prompting} ' \
        f'--n_times={n_times} ' \
        f'--prompt_for_shot_prompting_file={prompt_for_shot_prompting_file} ' \
        f'--prompt-path="{prompts_filepath}" ' \
        f'--response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/{benchmark_type}_responses_{shot_prompting}_shot.json" ' \
        f'--stat-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/{benchmark_type}_stat_{shot_prompting}_shot.json" '
    
    if model.endswith(".gguf"):
        command_to_execute_benchmark += f'--llm-under-test="LLAMACPP::{model}::random_string"'

    os.system(command_to_execute_benchmark)

    columns_from_json_response_file  = [
        "model", "language", "variant", "prompt_id", 
        "Execution time (s)", "CPU Energy (J)", "RAM Energy (J)", "GPU Energy (J)", 
                              "CPU Power (W)", "RAM Power (W)", "GPU Power (W)", 
                              "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                              "bleu_score"]
    
    autocompleteOrInstruct_json_to_csv(
        f"benchmarks/PurpleLlama/CybersecurityBenchmarks/results/{benchmark_type}_responses_{shot_prompting}_shot.json",
        f"benchmarks/PurpleLlama/CybersecurityBenchmarks/results/{benchmark_type}_stat_{shot_prompting}_shot.json", 
        f"results/cyberseceval/instruct_and_autocomplete_{shot_prompting}_shot.csv", 
        columns_from_json_response_file
        )

def run_mitre_benchmark(model: str, prompts_filepath: str, max_tokens: int, seed: int, 
                        n_ctx: int, top_p: float, temperature: float, 
                        save_output_flag: str, prompt_for_shot_prompting_file: str, 
                        SLEEP_TIME: float, shot_prompting: int, n_times: int):
    """
    Calculate the scores from the MITRE benchmark from CybersecEval.

    Args:
        model (str): LLM name.
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

    set_env_variables()
    model_short = os.path.splitext(os.path.basename(model))[0]

    #NOTE: These two LLMs are going to be the same in all the measurements.
    judge_llm     = JUDGE_LLM
    expansion_llm = EXPANSION_LLM

    command_to_execute_benchmark = (
        'python3 -m benchmarks.PurpleLlama.CybersecurityBenchmarks.benchmark.run '
        '--benchmark=mitre '
        f'--max_tokens={max_tokens} ' \
        f'--seed={seed} ' \
        f'--n_ctx={n_ctx} ' \
        f'--top_p={top_p} ' \
        f'--temperature={temperature} ' \
        f'--save_output_flag={save_output_flag} ' \
        f'--sleep_time={SLEEP_TIME} ' \
        f'--n_shot_prompting={shot_prompting} ' \
        f'--n_times={n_times} ' \
        f'--prompt_for_shot_prompting_file={prompt_for_shot_prompting_file} ' \
        f'--prompt-path="{prompts_filepath}" '
        f'--response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/mitre_responses.json" '
        f'--judge-response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/mitre_judge_responses.json" '
        f'--stat-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/mitre_stat.json" '
        f'--judge-llm="{judge_llm}" '
        f'--expansion-llm="{expansion_llm}"'
    )
    
    if model.endswith(".gguf"):
        command_to_execute_benchmark += f' --llm-under-test="LLAMACPP::{model}::random_string"'

    os.system(command_to_execute_benchmark)

    columns_from_json_response_file = [
        "model", "mitre_category", "prompt_id",
        "Execution time (s)", "CPU Energy (J)", "RAM Energy (J)", "GPU Energy (J)",
        "CPU Power (W)", "RAM Power (W)", "GPU Power (W)",
        "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)"
    ]

    mitre_json_to_csv(
        f'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/mitre_responses.json',
        f'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/mitre_stat.json',
        f'results/cyberseceval/mitre.csv',
        columns_from_json_response_file
    )


def run_interpreter_benchmark(model: str, prompts_filepath: str, max_tokens: int, seed: int, 
                              n_ctx: int, top_p: float, temperature: float, 
                              save_output_flag: str, prompt_for_shot_prompting_file: str, 
                              SLEEP_TIME: float, shot_prompting: int, n_times: int):
    """
    Calculate the scores from the Interpreter benchmark from CybersecEval.

    Args:
        model (str): LLM name.
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

    set_env_variables()
    model_short = os.path.splitext(os.path.basename(model))[0]

    #NOTE: This LLM will be the same in all the measurements.
    judge_llm     = JUDGE_LLM

    command_to_execute_benchmark = (
        'python3 -m benchmarks.PurpleLlama.CybersecurityBenchmarks.benchmark.run '
        '--benchmark=interpreter '
        f'--max_tokens={max_tokens} ' \
        f'--seed={seed} ' \
        f'--n_ctx={n_ctx} ' \
        f'--top_p={top_p} ' \
        f'--temperature={temperature} ' \
        f'--save_output_flag={save_output_flag} ' \
        f'--sleep_time={SLEEP_TIME} ' \
        f'--n_shot_prompting={shot_prompting} ' \
        f'--n_times={n_times} ' \
        f'--prompt_for_shot_prompting_file={prompt_for_shot_prompting_file} ' \
        f'--prompt-path="{prompts_filepath}" '
        f'--response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_responses.json" '
        f'--judge-response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_judge_responses.json" '
        f'--stat-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_stat.json" '
        f'--judge-llm="{judge_llm}" '
    )

    if model.endswith(".gguf"):
        command_to_execute_benchmark += f' --llm-under-test="LLAMACPP::{model}::random_string"'

    os.system(command_to_execute_benchmark)

    columns_from_json_response_file = [
        "model", "prompt_id", "attack_type", "Execution time (s)", "CPU Energy (J)",
        "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
        "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)"
    ]

    interpreter_json_to_csv(
        f'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_judge_responses.json',
        f'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_stat.json',
        f'results/cyberseceval/interpreter.csv',
        columns_from_json_response_file
    )

def run_frr_benchmark(model: str, prompts_filepath: str, max_tokens: int, seed: int, 
                      n_ctx: int, top_p: float, temperature: float, 
                      save_output_flag: str, prompt_for_shot_prompting_file: str, 
                      SLEEP_TIME: float, shot_prompting: int, n_times: int):
    """
    Calculate the scores from the False Rate Refusal benchmark from CybersecEval.

    Args:
        model (str): LLM name.
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

    set_env_variables()
    model_short = os.path.splitext(os.path.basename(model))[0]

    command_to_execute_benchmark = (
        'python3 -m benchmarks.PurpleLlama.CybersecurityBenchmarks.benchmark.run '
        '--benchmark=frr '
        f'--max_tokens={max_tokens} ' \
        f'--seed={seed} ' \
        f'--n_ctx={n_ctx} ' \
        f'--top_p={top_p} ' \
        f'--temperature={temperature} ' \
        f'--save_output_flag={save_output_flag} ' \
        f'--sleep_time={SLEEP_TIME} ' \
        f'--n_shot_prompting={shot_prompting} ' \
        f'--n_times={n_times} ' \
        f'--prompt_for_shot_prompting_file={prompt_for_shot_prompting_file} ' \
        f'--prompt-path="{prompts_filepath}" '
        f'--response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/frr_responses.json" '
        f'--stat-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/frr_stat.json" '
    )

    if model.endswith(".gguf"):
        command_to_execute_benchmark += f' --llm-under-test="LLAMACPP::{model}::random_string"'

    os.system(command_to_execute_benchmark)

    columns_from_json_response_file = [
        "model", "prompt_id", "attack_type", "Execution time (s)", "CPU Energy (J)",
        "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
        "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)", "judge_response", "language"
    ]

    frr_json_to_csv(
        f'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/frr_responses.json',
        f'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/frr_stat.json',
        f'results/cyberseceval/frr.csv',
        columns_from_json_response_file
    )

def run_canary_exploit_benchmark(model: str, prompts_filepath: str, max_tokens: int, seed: int, 
                      n_ctx: int, top_p: float, temperature: float, 
                      save_output_flag: str, prompt_for_shot_prompting_file: str, 
                      SLEEP_TIME: float, shot_prompting: int, n_times: int):
    """
    Calculate the scores from the Vulnerability Exploitation benchmark from CybersecEval.

    Args:
        model (str): LLM name.
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

    set_env_variables()
    model_short = os.path.splitext(os.path.basename(model))[0]

    command_to_execute_benchmark = (
        'python3 -m benchmarks.PurpleLlama.CybersecurityBenchmarks.benchmark.run '
        '--benchmark="canary-exploit" '
        f'--max_tokens={max_tokens} ' \
        f'--seed={seed} ' \
        f'--n_ctx={n_ctx} ' \
        f'--top_p={top_p} ' \
        f'--temperature={temperature} ' \
        f'--save_output_flag={save_output_flag} ' \
        f'--sleep_time={SLEEP_TIME} ' \
        f'--n_shot_prompting={shot_prompting} ' \
        f'--n_times={n_times} ' \
        f'--prompt_for_shot_prompting_file={prompt_for_shot_prompting_file} ' \
        f'--prompt-path="{prompts_filepath}" '
        f'--response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/canary_exploit_responses_{shot_prompting}_shot.json" '
        f'--judge-response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/canary_exploit_judge_responses_{shot_prompting}_shot.json" '
        f'--stat-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/canary_exploit_stat_{shot_prompting}_shot.json" '
    )

    if model.endswith(".gguf"):
        command_to_execute_benchmark += f' --llm-under-test="LLAMACPP::{model}::random_string"'

    os.system(command_to_execute_benchmark)

    columns_from_json_response_file = [
        "model", "prompt_id", "language", "challenge_type", "Execution time (s)", "CPU Energy (J)", 
        "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)", 
        "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)", "score"
    ]

    canary_exploit_json_to_csv(
        f'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/canary_exploit_judge_responses_{shot_prompting}_shot.json',
        f'results/cyberseceval/canary_exploit_{shot_prompting}_shot.csv',
        columns_from_json_response_file
    )