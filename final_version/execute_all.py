import json
import subprocess
import re
import csv
import os
import shlex
import time, sys

N_TIMES = 2

def execute_python_script(task_id, prompt, script_to_execute, CSV_FILENAME):
    # Prompt lido do ficheiro JSONL para um ficheiro de texto - resolve o problema do escaping!
    temp_prompt_file = "temp_prompt.txt"
    with open(temp_prompt_file, 'w') as prompt_file:
        prompt_file.write(prompt)

    command = f"python3 {script_to_execute} '{task_id}' {temp_prompt_file} {CSV_FILENAME}"

    subprocess.run(command, shell=True)


def start_measure(model_script, prompts_filepath):
    # Execução das scripts de todos os modelos considerados

    if prompts_filepath.endswith("HumanEval.jsonl"):
        # Este tratamento apenas se destina ao benchmark do HumanEval
        with open(prompts_filepath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                entry = json.loads(line)

                task_id = entry.get("task_id", "")
                prompt = entry.get("prompt", "")

                execute_python_script(task_id, prompt, model_script, FILENAME)
    else:
        print("Ficheiro JSONL não pertence a nenhum benchmark considerado")


if __name__ == "__main__":

    # Nome do CSV final
    FILENAME = "measurements.csv"

    subprocess.run("sudo chmod -R a+r /sys/class/powercap/intel-rapl", shell=True)

    # Nome das colunas do CSV final
    header_list = [
                   "LLM",
                   "Benchmark prompt",
                   "Execution time",
                   "Package",
                   "DRAM",
                   "HumanEval pass@1"
                  ]

    if not os.path.isfile(FILENAME) or os.stat(FILENAME).st_size == 0:
        # Se o ficheiro não existir, então cria-se
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header_list)

    # Nome dos prompts a considerar
    prompt_files = [
        "human_eval/data/HumanEval.jsonl"
    ]

    # Nome das scripts a executar
    scripts_to_execute = [
        "llama-2-7b.Q2_K.py",
        "llama-2-7b.Q3_K_L.py"
    ]

    for i in range(N_TIMES):
        print(f"------------------ Executed times = {i} ------------------\n")
        for script in scripts_to_execute:
            for prompt_file in prompt_files:
                start_measure(script, prompt_file)