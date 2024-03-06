import json, csv, os, time
import benchmarks_execution_scripts.humaneval_x as humaneval_x
import benchmarks_execution_scripts.utils as benchmark_utils
from measure_utils import extract_llm_name

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

def start_measure(llm_path, prompts_filepath, max_tokens):
    # Execução das scripts de todos os modelos considerados

    if prompts_filepath.endswith(
        ("humaneval_cpp.jsonl", "humaneval_go.jsonl", "humaneval_java.jsonl", 
         "humaneval_js.jsonl", "humaneval_python.jsonl")):
        # Este tratamento apenas se destina ao benchmark do HumanEval
        #NOTE: Caso haja algo estranho no append dos scores dos benchmarks, atualizar esta função 
        # (ver https://github.com/simaocunha71/thesis-repository/tree/ab63a74720a048bc4b8ed8fa14e6275670cc5fbe)
        with open(prompts_filepath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                entry = json.loads(line)

                task_id = entry.get("task_id", "")
                prompt = entry.get("prompt", "")

                if prompts_filepath.endswith("humaneval_cpp.jsonl"):
                    execute_python_script(task_id, prompt, llm_path, FILENAME, max_tokens, "cpp")
                elif prompts_filepath.endswith("humaneval_go.jsonl"):
                    execute_python_script(task_id, prompt, llm_path, FILENAME, max_tokens, "go")
                elif prompts_filepath.endswith("humaneval_java.jsonl"):
                    execute_python_script(task_id, prompt, llm_path, FILENAME, max_tokens, "java")
                elif prompts_filepath.endswith("humaneval_js.jsonl"):
                    execute_python_script(task_id, prompt, llm_path, FILENAME, max_tokens, "js")
                elif prompts_filepath.endswith("humaneval_python.jsonl"):
                    execute_python_script(task_id, prompt, llm_path, FILENAME, max_tokens, "python")

        # Todos os benchmarks apenas vão ser executados depois de as LLMs responderem a todos os prompts
        human_eval_score = humaneval_x.run_human_eval_benchmark(extract_llm_name(llm_path), prompts_filepath.split('_')[-1].split('.')[0])
        benchmark_utils.add_score_in_csv(FILENAME, FILENAME, "HumanEval-X", human_eval_score)

    else:
        print("Ficheiro JSONL não pertence a nenhum benchmark considerado")


if __name__ == "__main__":

    # Nome do CSV final
    FILENAME = "measurements.csv"

    # Nome das colunas do CSV final
    header_list = [
                   "LLM",
                   "Benchmark prompt",
                   "Execution time (s)",
                   "CPU Energy (J)",
                   "RAM Energy (J)",
                   "GPU Energy (J)",
                   "CPU Power (W)", 
                   "RAM Power (W)",
                   "GPU Power (W)",
                   "CO2 emissions (Kg)",
                   "CO2 emissions rate (Kg/s)",
                   "HumanEval-X"
                  ]

    if not os.path.isfile(FILENAME) or os.stat(FILENAME).st_size == 0:
        # Se o ficheiro não existir, então cria-se
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header_list)

    # Nome dos prompts a considerar
    prompt_files = [
        "prompts/humaneval_x/humaneval_cpp.jsonl",
        "prompts/humaneval_x/humaneval_go.jsonl",
        "prompts/humaneval_x/humaneval_java.jsonl",
        "prompts/humaneval_x/humaneval_js.jsonl",
        "prompts/humaneval_x/humaneval_python.jsonl"
    ]

    # Path das LLMs a executar
    llms_to_execute = [
        "llama_c++/models/llama-2-7b.Q2_K.gguf",
        "llama_c++/models/llama-2-7b.Q3_K_L.gguf"
    ]

    # Tokens máximos a serem considerados pelas LLMs
    max_tokens = 512

    for i in range(N_TIMES):
        print(f"------------------ Executed times = {i+1} ------------------\n")
        for llm_path in llms_to_execute:
            for prompt_file in prompt_files:
                start_measure(llm_path, prompt_file, max_tokens)
                time.sleep(5)