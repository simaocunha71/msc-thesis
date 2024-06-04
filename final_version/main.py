import argparse, json, csv, os, time, sys
from benchmarks.benchmarks_execution_scripts import humaneval_x, cyberseceval, mbpp
from benchmarks.benchmarks_execution_scripts import utils as benchmark_utils
from measure_utils import extract_llm_name, create_csv, change_max_tokens_value, change_n_ctx_value, change_seed_value, change_boolean_to_save_outputs, validate_supported_models

def execute_python_script(task_id, prompt, llm_path, CSV_FILENAME, max_tokens, benchmark_type, n_ctx, seed, language=None):
    # Prompt lido do ficheiro JSONL para um ficheiro de texto - resolve o problema do escaping!
    temp_prompt_file = "temp_prompt.txt"
    with open(temp_prompt_file, 'w') as prompt_file:
        prompt_file.write(prompt)

    if llm_path.endswith(".gguf"):
        command = f"python3 llms/llamacpp_wrapper.py '{task_id}' '{temp_prompt_file}' '{CSV_FILENAME}' '{llm_path}' {max_tokens} '{benchmark_type}' '{n_ctx}' '{seed}'"
    else:
        print(f"Não existe script capaz de executar o LLM com o path {llm_path}")
        sys.exit(-1)

    if language:
        command += f" {language}"
    os.system(command)

def start_measure(llm_path_list, prompts_filepath_list, max_tokens, n_ctx, seed):
    # Execução das scripts de todos os modelos considerados

    for llm_path in llm_path_list:
        for prompts_filepath in prompts_filepath_list:

            if "humaneval_x" in prompts_filepath:
                # Este tratamento apenas se destina ao benchmark do HumanEval-X
                with open(prompts_filepath, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        entry = json.loads(line)

                        task_id = entry.get("task_id", "")
                        prompt = entry.get("prompt", "")

                        if prompts_filepath.endswith("humaneval_cpp.jsonl"):
                            execute_python_script(task_id, prompt, llm_path, os.path.join("results", "humaneval_x", "humaneval_x.csv"), max_tokens, "humaneval_x", n_ctx, seed, "cpp")
                        elif prompts_filepath.endswith("humaneval_go.jsonl"):
                            execute_python_script(task_id, prompt, llm_path, os.path.join("results", "humaneval_x", "humaneval_x.csv"), max_tokens, "humaneval_x", n_ctx, seed, "go")
                        elif prompts_filepath.endswith("humaneval_java.jsonl"):
                            execute_python_script(task_id, prompt, llm_path, os.path.join("results", "humaneval_x", "humaneval_x.csv"), max_tokens, "humaneval_x", n_ctx, seed, "java")
                        elif prompts_filepath.endswith("humaneval_js.jsonl"):
                            execute_python_script(task_id, prompt, llm_path, os.path.join("results", "humaneval_x", "humaneval_x.csv"), max_tokens, "humaneval_x", n_ctx, seed, "js")
                        elif prompts_filepath.endswith("humaneval_python.jsonl"):
                            execute_python_script(task_id, prompt, llm_path, os.path.join("results", "humaneval_x", "humaneval_x.csv"), max_tokens, "humaneval_x", n_ctx, seed, "python")
                        elif prompts_filepath.endswith("humaneval_rust.jsonl"):
                            execute_python_script(task_id, prompt, llm_path, os.path.join("results", "humaneval_x", "humaneval_x.csv"), max_tokens, "humaneval_x", n_ctx, seed, "rust")

                # Todos os benchmarks apenas vão ser executados depois de as LLMs responderem a todos os prompts
                human_eval_score = humaneval_x.run_human_eval_benchmark(extract_llm_name(llm_path), prompts_filepath.split('_')[-1].split('.')[0])
                benchmark_utils.add_score_in_csv(os.path.join("results", "humaneval_x", "humaneval_x.csv"), os.path.join("results", "humaneval_x", "humaneval_x.csv"), "HumanEval-X", human_eval_score)
                time.sleep(5)

            elif "cyberseceval" in prompts_filepath:
                # Create the results/cyberseceval folder if it doesn't exist
                folder_path = os.path.join("results", "cyberseceval")
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # This treatment is only for the CyberSecEval benchmark
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
            elif "mbpp" in prompts_filepath:
                # Este tratamento apenas se destina ao benchmark do MBPP
                with open(prompts_filepath, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        entry = json.loads(line)

                        task_id = entry.get("task_id", "")
                        prompt = entry.get("prompt", "")

                        execute_python_script(str(task_id), prompt, llm_path, os.path.join("results", "mbpp", "mbpp.csv"), max_tokens, "mbpp", n_ctx, seed)

                # Todos os benchmarks apenas vão ser executados depois de as LLMs responderem a todos os prompts
                mbpp_pass1, mbppPlus_pass1 = mbpp.run_mbpp_benchmark(extract_llm_name(llm_path))
                benchmark_utils.add_score_in_csv(os.path.join("results", "mbpp", "mbpp.csv"), os.path.join("results", "mbpp", "mbpp.csv"), "MBPP pass@1", mbpp_pass1)
                benchmark_utils.add_score_in_csv(os.path.join("results", "mbpp", "mbpp.csv"), os.path.join("results", "mbpp", "mbpp.csv"), "MBPP+ pass@1", mbppPlus_pass1)
                time.sleep(5)
            else:
                print("Ficheiro JSONL não pertence a nenhum benchmark considerado")
        
        try:
            os.system("rm -rf ~/.cache/evalplus/*")
        except:
            pass
        

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
    parser.add_argument("--save_output", type=str, default=512, help="'yes' to save LLM outputs in files, 'no' otherwise.")

    args = parser.parse_args()

    llm_path_list = args.llm_path
    benchmarks = args.benchmarks
    max_tokens = args.max_tokens
    n_ctx = args.n_ctx
    seed = args.seed
    N_TIMES = args.n_times
    save_output_flag = args.save_output

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
                    "HumanEval-X"
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
                    "Is extremely malicious",
                    "Is potentially malicious",
                    "Is non malicious",
                    "Total count",
                    "Malicious percentage"
                ]
            elif "cyberseceval/frr" in b:
                csv_files["frr"] = [
                    "LLM", "Prompt ID", "Attack type", "Execution time (s)", "CPU Energy (J)",
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
                    "Is extremely malicious",
                    "Is potentially malicious",
                    "Is non malicious",
                    "Total count",
                    "Malicious percentage"
                ]
                csv_files["frr"] = [
                    "LLM", "Prompt ID", "Attack type", "Execution time (s)", "CPU Energy (J)",
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
                    "MBPP pass@1", "MBPP+ pass@1"
                ]            
            elif "all" in b:
                csv_files["humaneval_x"] = [
                    "LLM", "Benchmark prompt", "Execution time (s)", "CPU Energy (J)",
                    "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                    "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                    "HumanEval-X"
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
                    "Is extremely malicious",
                    "Is potentially malicious",
                    "Is non malicious",
                    "Total count",
                    "Malicious percentage"
                ]
                csv_files["frr"] = [
                    "LLM", "Prompt ID", "Attack type", "Execution time (s)", "CPU Energy (J)",
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
                    "MBPP pass@1", "MBPP+ pass@1"
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
            start_measure(llm_path_list, prompts_filepath_list, max_tokens, n_ctx, seed)

if __name__ == "__main__":
    main()
