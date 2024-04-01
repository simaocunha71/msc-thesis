import argparse
import json
import csv
import os
import time
import sys
from benchmarks_execution_scripts import humaneval_x
from benchmarks_execution_scripts import cyberseceval
from benchmarks_execution_scripts import utils as benchmark_utils
from measure_utils import extract_llm_name, create_csv, change_max_tokens_value

N_TIMES = 1

def execute_python_script(task_id, prompt, llm_path, CSV_FILENAME, max_tokens, language=None):
    # Prompt lido do ficheiro JSONL para um ficheiro de texto - resolve o problema do escaping!
    temp_prompt_file = "temp_prompt.txt"
    with open(temp_prompt_file, 'w') as prompt_file:
        prompt_file.write(prompt)

    if llm_path.endswith(".gguf"):
        command = f"python3 llamacpp_wrapper.py '{task_id}' '{temp_prompt_file}' '{CSV_FILENAME}' '{llm_path}' {max_tokens}"
    else:
        print(f"Não existe script capaz de executar o LLM com o path {llm_path}")
        sys.exit(-1)

    if language:
        command += f" {language}"

    os.system(command)

def start_measure(llm_path_list, prompts_filepath_list, max_tokens):
    # Execução das scripts de todos os modelos considerados

    for llm_path in llm_path_list:
        for prompts_filepath in prompts_filepath_list:

            if "humaneval_x" in prompts_filepath:
                # Este tratamento apenas se destina ao benchmark do HumanEval-X
                #NOTE: Caso haja algo estranho no append dos scores dos benchmarks, atualizar esta função
                # (ver https://github.com/simaocunha71/thesis-repository/tree/ab63a74720a048bc4b8ed8fa14e6275670cc5fbe)
                with open(prompts_filepath, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        entry = json.loads(line)

                        task_id = entry.get("task_id", "")
                        prompt = entry.get("prompt", "")

                        if prompts_filepath.endswith("humaneval_cpp.jsonl"):
                            execute_python_script(task_id, prompt, llm_path, "measurements_humaneval.csv", max_tokens, "cpp")
                        elif prompts_filepath.endswith("humaneval_go.jsonl"):
                            execute_python_script(task_id, prompt, llm_path, "measurements_humaneval.csv", max_tokens, "go")
                        elif prompts_filepath.endswith("humaneval_java.jsonl"):
                            execute_python_script(task_id, prompt, llm_path, "measurements_humaneval.csv", max_tokens, "java")
                        elif prompts_filepath.endswith("humaneval_js.jsonl"):
                            execute_python_script(task_id, prompt, llm_path, "measurements_humaneval.csv", max_tokens, "js")
                        elif prompts_filepath.endswith("humaneval_python.jsonl"):
                            execute_python_script(task_id, prompt, llm_path, "measurements_humaneval.csv", max_tokens, "python")

                # Todos os benchmarks apenas vão ser executados depois de as LLMs responderem a todos os prompts
                human_eval_score = humaneval_x.run_human_eval_benchmark(extract_llm_name(llm_path), prompts_filepath.split('_')[-1].split('.')[0])
                benchmark_utils.add_score_in_csv("measurements_humaneval.csv", "measurements_humaneval.csv", "HumanEval-X", human_eval_score)
                time.sleep(5)

            elif "cyberseceval" in prompts_filepath:
                # Este tratamento apenas se destina ao benchmark do CyberSecEval
                if "autocomplete" in prompts_filepath:
                    cyberseceval.run_instruct_or_autocomplete_benchmark(llm_path, prompts_filepath, "autocomplete")

                elif "instruct" in prompts_filepath:
                    cyberseceval.run_instruct_or_autocomplete_benchmark(llm_path, prompts_filepath, "instruct")

                elif "mitre" in prompts_filepath:
                    cyberseceval.run_mitre_benchmark(llm_path, prompts_filepath)

            else:
                print("Ficheiro JSONL não pertence a nenhum benchmark considerado")

def main():
    parser = argparse.ArgumentParser(description="Execute benchmarks with given arguments.")
    parser.add_argument("--llm_path", nargs='+', help="Path to the LLMs to execute.")
    parser.add_argument("--benchmarks", nargs='+', choices=["humaneval_x","humaneval_x/c++", "humaneval_x/go", "humaneval_x/java",
                                                 "humaneval_x/javascript", "humaneval_x/python", 
                                                 "cyberseceval", "cyberseceval/autocomplete", "cyberseceval/instruct", "cyberseceval/mitre",
                                                 "all"], help="Choose benchmarks to run.")
    parser.add_argument("--max_tokens", type=int, default=512, help="Maximum tokens.")
    args = parser.parse_args()

    llm_path_list = args.llm_path
    benchmarks = args.benchmarks
    max_tokens = args.max_tokens

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
            "prompts/cyberseceval/autocomplete.json",
            "prompts/cyberseceval/instruct.json",
            "prompts/cyberseceval/mitre_benchmark_100_per_category_with_augmentation.json"
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
                    "prompts/humaneval_x/humaneval_python.jsonl"
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
            elif benchmark == "cyberseceval":
                prompts_filepath_list.extend([
                    "prompts/cyberseceval/autocomplete.json",
                    "prompts/cyberseceval/instruct.json",
                    "prompts/cyberseceval/mitre_benchmark_100_per_category_with_augmentation.json"
                ])
            elif benchmark == "cyberseceval/autocomplete":
                prompts_filepath_list.append("prompts/cyberseceval/autocomplete.json")
            elif benchmark == "cyberseceval/instruct":
                prompts_filepath_list.append("prompts/cyberseceval/instruct.json")
            elif benchmark == "cyberseceval/mitre":
                prompts_filepath_list.append("prompts/cyberseceval/mitre_benchmark_100_per_category_with_augmentation.json")
            else:
                print(f"Invalid value '{benchmark}' for --benchmarks.")
                sys.exit(1)

    # Define CSV files and their columns based on the benchmarks
    csv_files = {}
    print(benchmarks)
    for b in benchmarks:
        if "humaneval_x" in b:
            csv_files["measurements_humaneval"] = [
                "LLM", "Benchmark prompt", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "HumanEval-X"
            ]
        elif "cyberseceval/autocomplete" in b or "cyberseceval/instruct" in b:
            csv_files["measurements_instructAndAutocomplete"] = [
                "LLM", "Benchmark prompt", "Language", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Bleu score", "Total count", "Vulnerable percentage",
                "Vulnerable suggestion count", "Pass rate"
            ]
        elif "cyberseceval/mitre" in b:
            csv_files["measurements_mitre"] = [
                "LLM", "Benchmark prompt", "Category", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Refusal count", "Malicious count", "Benign count",
                "Total count", "Benign percentage", "Else count"
            ]
        elif "cyberseceval" in b:
            csv_files["measurements_instructAndAutocomplete"] = [
                "LLM", "Benchmark prompt", "Language", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Bleu score", "Total count", "Vulnerable percentage",
                "Vulnerable suggestion count", "Pass rate"
            ]        
            csv_files["measurements_mitre"] = [
                "LLM", "Benchmark prompt", "Category", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Refusal count", "Malicious count", "Benign count",
                "Total count", "Benign percentage", "Else count"
            ]
    
    print(csv_files)
    # Create the CSV files
    for filename, columns in csv_files.items():
        create_csv(filename + ".csv", columns)

    change_max_tokens_value("CybersecurityBenchmarks/benchmark/llm.py", max_tokens)
    start_measure(llm_path_list, prompts_filepath_list, max_tokens)

if __name__ == "__main__":
    main()
