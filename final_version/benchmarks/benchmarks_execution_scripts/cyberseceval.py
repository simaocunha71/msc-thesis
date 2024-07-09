import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import autocompleteOrInstruct_json_to_csv, mitre_json_to_csv, interpreter_json_to_csv, frr_json_to_csv, canary_exploit_json_to_csv

def run_instruct_or_autocomplete_benchmark(model, prompts_filepath, benchmark_type):
    """Calcula os scores do benchmark Instruct ou Autocomplete do CybersecEval"""

    #Variáveis de ambiente necessárias para a execução do benchmark
    #os.system("export WEGGLI_PATH=weggli")
    os.environ['WEGGLI_PATH'] = 'weggli'
    #os.system('export PATH="$HOME/.cargo/bin:$PATH"')
    os.environ['PATH'] = f"{os.environ['HOME']}/.cargo/bin:{os.environ['PATH']}"

    command_to_execute_benchmark = f'python3 -m benchmarks.PurpleLlama.CybersecurityBenchmarks.benchmark.run ' \
        f'--benchmark={benchmark_type} ' \
        f'--prompt-path="{prompts_filepath}" ' \
        f'--response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/{benchmark_type}_responses.json" ' \
        f'--stat-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/{benchmark_type}_stat.json" '
    
    #Adiciona a natureza do LLM nestes if-else
    if "llama_c++" in model:
        command_to_execute_benchmark += f'--llm-under-test="LLAMACPP::{model}::random_string"'

    os.system(command_to_execute_benchmark)

    columns_from_json_response_file  = [
        "model", "language", "variant", "prompt_id", 
        "Execution time (s)", "CPU Energy (J)", "RAM Energy (J)", "GPU Energy (J)", 
                              "CPU Power (W)", "RAM Power (W)", "GPU Power (W)", 
                              "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                              "bleu_score"]

    autocompleteOrInstruct_json_to_csv(
        f"benchmarks/PurpleLlama/CybersecurityBenchmarks/results/{benchmark_type}_responses.json",
        f"benchmarks/PurpleLlama/CybersecurityBenchmarks/results/{benchmark_type}_stat.json", 
        "results/cyberseceval/instruct_and_autocomplete.csv", 
        columns_from_json_response_file
        )

def run_mitre_benchmark(model, prompts_filepath):
    'Calcula os scores do benchmark MITRE do CybersecEval'

    #Variáveis de ambiente necessárias para a execução do benchmark
    os.environ['WEGGLI_PATH'] = 'weggli'
    os.environ['PATH'] = f"{os.environ['HOME']}/.cargo/bin:{os.environ['PATH']}"

    #Estas duas LLMs vão estar fixadas para todas as medições
    judge_llm     = "LLAMACPP::llms/llama_c++/models/llama-2-7b.Q3_K_L.gguf::random_string"
    expansion_llm = "LLAMACPP::llms/llama_c++/models/llama-2-7b.Q3_K_S.gguf::random_string"

    command_to_execute_benchmark = (
        'python3 -m benchmarks.PurpleLlama.CybersecurityBenchmarks.benchmark.run '
        '--benchmark=mitre '
        f'--prompt-path="{prompts_filepath}" '
        '--response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/mitre_responses.json" '
        '--judge-response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/mitre_judge_responses.json" '
        '--stat-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/mitre_stat.json" '
        f'--judge-llm="{judge_llm}" '
        f'--expansion-llm="{expansion_llm}"'
    )
    
    if "llama_c++" in model:
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
        'results/cyberseceval/mitre.csv',
        columns_from_json_response_file
    )

def run_interpreter_benchmark(model, prompts_filepath):
    'Calcula os scores do benchmark Interpreter do CybersecEval'

    #Variáveis de ambiente necessárias para a execução do benchmark
    os.environ['WEGGLI_PATH'] = 'weggli'
    os.environ['PATH'] = f"{os.environ['HOME']}/.cargo/bin:{os.environ['PATH']}"

    #Esta LLM vai estar fixada para todas as medições
    judge_llm     = "LLAMACPP::llms/llama_c++/models/llama-2-7b.Q3_K_L.gguf::random_string"

    command_to_execute_benchmark = (
        'python3 -m benchmarks.PurpleLlama.CybersecurityBenchmarks.benchmark.run '
        '--benchmark=interpreter '
        f'--prompt-path="{prompts_filepath}" '
        '--response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_responses.json" '
        '--judge-response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_judge_responses.json" '
        '--stat-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_stat.json" '
        f'--judge-llm="{judge_llm}" '
    )

    if "llama_c++" in model:
        command_to_execute_benchmark += f' --llm-under-test="LLAMACPP::{model}::random_string"'

    os.system(command_to_execute_benchmark)


    columns_from_json_response_file = [
        "model", "prompt_id", "attack_type", "Execution time (s)", "CPU Energy (J)",
        "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
        "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
    ]

    interpreter_json_to_csv(
        'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_responses.json',
        'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/interpreter_stat.json',
        'results/cyberseceval/interpreter.csv',
        columns_from_json_response_file
    )

def run_frr_benchmark(model, prompts_filepath):
    'Calcula os scores do benchmark False Rate Refusal do CybersecEval'

    #Variáveis de ambiente necessárias para a execução do benchmark
    os.environ['WEGGLI_PATH'] = 'weggli'
    os.environ['PATH'] = f"{os.environ['HOME']}/.cargo/bin:{os.environ['PATH']}"

    #Esta LLM vai estar fixada para todas as medições
    judge_llm     = "LLAMACPP::llms/llama_c++/models/llama-2-7b.Q3_K_L.gguf::random_string"

    command_to_execute_benchmark = (
        'python3 -m benchmarks.PurpleLlama.CybersecurityBenchmarks.benchmark.run '
        '--benchmark=frr '
        f'--prompt-path="{prompts_filepath}" '
        '--response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/frr_responses.json" '
        '--stat-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/frr_stat.json" '
    )

    if "llama_c++" in model:
        command_to_execute_benchmark += f' --llm-under-test="LLAMACPP::{model}::random_string"'

    os.system(command_to_execute_benchmark)


    columns_from_json_response_file = [
        "model", "prompt_id", "attack_type", "Execution time (s)", "CPU Energy (J)",
        "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
        "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)", "judge_response"
    ]

    frr_json_to_csv(
        'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/frr_responses.json',
        'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/frr_stat.json',
        'results/cyberseceval/frr.csv',
        columns_from_json_response_file
    )

def run_canary_exploit_benchmark(model, prompts_filepath):
    'Calcula os scores do benchmark Vulnerability Exploitation do CybersecEval'

    #Variáveis de ambiente necessárias para a execução do benchmark
    os.environ['WEGGLI_PATH'] = 'weggli'
    os.environ['PATH'] = f"{os.environ['HOME']}/.cargo/bin:{os.environ['PATH']}"

    #Esta LLM vai estar fixada para todas as medições
    judge_llm     = "LLAMACPP::llms/llama_c++/models/llama-2-7b.Q3_K_L.gguf::random_string"

    command_to_execute_benchmark = (
        'python3 -m benchmarks.PurpleLlama.CybersecurityBenchmarks.benchmark.run '
        '--benchmark=canary-exploit '
        f'--prompt-path="{prompts_filepath}" '
        '--response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/canary_exploit_responses.json" '
        '--judge-response-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/canary_exploit_judge_responses.json" '
        '--stat-path="benchmarks/PurpleLlama/CybersecurityBenchmarks/results/canary_exploit_stat.json" '
    )

    if "llama_c++" in model:
        command_to_execute_benchmark += f' --llm-under-test="LLAMACPP::{model}::random_string"'

    os.system(command_to_execute_benchmark)


    columns_from_json_response_file = [
        "model", "prompt_id", "language", "challenge_type", "Execution time (s)", "CPU Energy (J)",
        "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
        "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)"
    ]

    canary_exploit_json_to_csv(
        'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/canary_exploit_responses.json',
        'benchmarks/PurpleLlama/CybersecurityBenchmarks/results/canary_exploit_stat.json',
        'results/cyberseceval/canary_exploit.csv',
        columns_from_json_response_file
    )