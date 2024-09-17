import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import autocompleteOrInstruct_json_to_csv, mitre_json_to_csv, interpreter_json_to_csv, frr_json_to_csv, canary_exploit_json_to_csv

# Global definitions for LLMs
JUDGE_LLM = "LLAMACPP::llms/models/orca-2-13b.Q3_K_M.gguf::random_string"
EXPANSION_LLM = "LLAMACPP::llms/models/Tess-10.7B-v2.0-Q6_K.gguf::random_string"

def set_env_variables():
    #Variáveis de ambiente necessárias para a execução do benchmark

    #os.system("export WEGGLI_PATH=weggli")
    os.environ['WEGGLI_PATH'] = 'weggli'
    #os.system('export PATH="$HOME/.cargo/bin:$PATH"')
    os.environ['PATH'] = f"{os.environ['HOME']}/.cargo/bin:{os.environ['PATH']}"

def run_instruct_or_autocomplete_benchmark(model, prompts_filepath, benchmark_type, max_tokens, seed, n_ctx, top_p, temperature, save_output_flag, prompt_for_shot_prompting_file, SLEEP_TIME, shot_prompting):
    """Calcula os scores do benchmark Instruct ou Autocomplete do CybersecEval"""

    set_env_variables()

    command_to_execute_benchmark = f'python3 -m benchmarks.PurpleLlama.CybersecurityBenchmarks.benchmark.run ' \
        f'--benchmark={benchmark_type} ' \
        f'--max_tokens={max_tokens} ' \
        f'--seed={seed} ' \
        f'--n_ctx={n_ctx} ' \
        f'--top_p={top_p} ' \
        f'--temperature={temperature} ' \
        f'--save_output_flag={save_output_flag} ' \
        f'--sleep_time={SLEEP_TIME} ' \
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

def run_mitre_benchmark(model, prompts_filepath, max_tokens, seed, n_ctx, top_p, temperature, save_output_flag, prompt_for_shot_prompting_file, SLEEP_TIME, shot_prompting):
    'Calcula os scores do benchmark MITRE do CybersecEval'

    set_env_variables()

    #Estas duas LLMs vão estar fixadas para todas as medições
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
        f'--prompt_for_shot_prompting_file={prompt_for_shot_prompting_file} ' \
        f'--prompt-path="{prompts_filepath}" '
        '--response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/mitre_responses.json" '
        '--judge-response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/mitre_judge_responses.json" '
        '--stat-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/mitre_stat.json" '
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
        'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/mitre_responses.json',
        'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/mitre_stat.json',
        f'results/cyberseceval/mitre.csv',
        columns_from_json_response_file
    )

def run_interpreter_benchmark(model, prompts_filepath, max_tokens, seed, n_ctx, top_p, temperature, save_output_flag, prompt_for_shot_prompting_file, SLEEP_TIME, shot_prompting):
    'Calcula os scores do benchmark Interpreter do CybersecEval'

    set_env_variables()

    #Esta LLM vai estar fixada para todas as medições
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
        f'--prompt_for_shot_prompting_file={prompt_for_shot_prompting_file} ' \
        f'--prompt-path="{prompts_filepath}" '
        '--response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_responses.json" '
        '--judge-response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_judge_responses.json" '
        '--stat-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_stat.json" '
        f'--judge-llm="{judge_llm}" '
    )

    if model.endswith(".gguf"):
        command_to_execute_benchmark += f' --llm-under-test="LLAMACPP::{model}::random_string"'

    os.system(command_to_execute_benchmark)


    columns_from_json_response_file = [
        "model", "prompt_id", "attack_type", "Execution time (s)", "CPU Energy (J)",
        "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
        "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)", "maliciousness_level"
    ]

    interpreter_json_to_csv(
        'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_judge_responses.json',
        'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_stat.json',
        f'results/cyberseceval/interpreter.csv',
        columns_from_json_response_file
    )

def run_frr_benchmark(model, prompts_filepath, max_tokens, seed, n_ctx, top_p, temperature, save_output_flag, prompt_for_shot_prompting_file, SLEEP_TIME, shot_prompting):
    'Calcula os scores do benchmark False Rate Refusal do CybersecEval'

    set_env_variables()

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
        f'--prompt_for_shot_prompting_file={prompt_for_shot_prompting_file} ' \
        f'--prompt-path="{prompts_filepath}" '
        '--response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/frr_responses.json" '
        '--stat-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/frr_stat.json" '
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
        'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/frr_responses.json',
        'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/frr_stat.json',
        f'results/cyberseceval/frr.csv',
        columns_from_json_response_file
    )

def run_canary_exploit_benchmark(model, prompts_filepath, max_tokens, seed, n_ctx, top_p, temperature, save_output_flag, prompt_for_shot_prompting_file, SLEEP_TIME, shot_prompting):
    'Calcula os scores do benchmark Vulnerability Exploitation do CybersecEval'

    set_env_variables()

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
        f'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/canary_exploit_stat.json_{shot_prompting}_shot',
        f'results/cyberseceval/canary_exploit_{shot_prompting}_shot.csv',
        columns_from_json_response_file
    )