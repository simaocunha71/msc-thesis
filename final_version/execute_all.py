import json
import subprocess
import re
import csv
import os
import shlex
import time, sys

N_TIMES = 2

def get_scripts():
    """Junta todas as scripts que executam os LLMs numa lista"""
    scripts = []
    scripts.append('llama-2-7b.Q2_K.py')
    return scripts

def execute_python_script(task_id, prompt, script_to_execute, CSV_FILENAME):
    # Escreva o prompt em um arquivo temporário
    temp_prompt_file = "temp_prompt.txt"
    with open(temp_prompt_file, 'w') as prompt_file:
        prompt_file.write(prompt)

    # Componha o comando para executar o Python script com o caminho do arquivo prompt
    command = f"python3 {script_to_execute} '{task_id}' {temp_prompt_file} {CSV_FILENAME}"

    # Execute o comando usando o shell
    subprocess.run(command, shell=True)


def start_measure(prompts_filepath):
    # Execução das scripts de todos os modelos considerados

    if prompts_filepath.endswith("HumanEval.jsonl"):
        # Este tratamento apenas se destina ao benchmark do HumanEval
        with open(prompts_filepath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                entry = json.loads(line)

                task_id = entry.get("task_id", "")
                prompt = entry.get("prompt", "")

                scripts_to_execute = get_scripts()

                for script in scripts_to_execute:
                    execute_python_script(task_id, prompt, script, FILENAME)
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

    for prompt_file in prompt_files:
        for _ in range(N_TIMES):
            start_measure(prompt_file)