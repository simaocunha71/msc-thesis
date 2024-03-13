import os
import sys
# Adicione o diretório atual ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import autocompleteOrInstruct_json_to_csv

def run_instruct_or_autocomplete_benchmark(model, benchmark_type):
    """Calcula os scores do benchmark Instruct ou Autocomplete do CybersecEval"""

    #Variáveis de ambiente necessárias para a execução do benchmark
    #os.system("export WEGGLI_PATH=weggli")
    os.environ['WEGGLI_PATH'] = 'weggli'
    #os.system('export PATH="$HOME/.cargo/bin:$PATH"')
    os.environ['PATH'] = f"{os.environ['HOME']}/.cargo/bin:{os.environ['PATH']}"

    command_to_execute_benchmark = f'python3 -m CybersecurityBenchmarks.benchmark.run ' \
        f'--benchmark={benchmark_type} ' \
        f'--prompt-path="prompts/cyberseceval/{benchmark_type}.json" ' \
        f'--response-path="CybersecurityBenchmarks/results/{benchmark_type}_responses.json" ' \
        f'--stat-path="CybersecurityBenchmarks/results/{benchmark_type}_stat.json" '
    
    if "llama_c++" in model:
        command_to_execute_benchmark += f'--llm-under-test="LLAMACPP::{model}::random_string"'

    os.system(command_to_execute_benchmark)

    columns_from_json_response_file  = [
        "model", "variant", "prompt_id", 
        "Execution time (s)", "CPU Energy (J)", "RAM Energy (J)", "GPU Energy (J)", 
                              "CPU Power (W)", "RAM Power (W)", "GPU Power (W)", 
                              "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)"]

    autocompleteOrInstruct_json_to_csv(
        f"CybersecurityBenchmarks/results/{benchmark_type}_responses.json",
        f"CybersecurityBenchmarks/results/{benchmark_type}_stat.json", 
        "measurements_instructAndAutocomplete.csv", 
        columns_from_json_response_file
        )
