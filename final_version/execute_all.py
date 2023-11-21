import json
import subprocess
import re
import csv
import os
import shlex
import time, sys

N_TIMES = 1

def add_human_eval_score_in_csv(csv_file_old, csv_file_new, column_name, value_to_add):
    """Adiciona um valor numa coluna de um ficheiro CSV já existente"""
    
    # Lê o ficheiro CSV de entrada (s/ o HumanEvalScore)
    with open(csv_file_old, 'r') as csv_in:
        reader = csv.DictReader(csv_in)
        header = reader.fieldnames

        # Verifica se a coluna à qual queremos adicionar o score existe no ficheiro CSV de input
        if column_name not in header:
            raise ValueError(f"A coluna '{column_name}' não existe no ficheiro CSV de input.")

        # Lê todas as linhas e preenche os valores na coluna específica com o valor dado do score
        rows = list(reader)
        for row in rows:
            if column_name not in row or not row[column_name]:
                row[column_name] = value_to_add

    # Escreve o ficheiro CSV de output
    with open(csv_file_new, 'w', newline='') as csv_out:
        writer = csv.DictWriter(csv_out, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)

def run_human_eval_benchmark(model):
    """Calcula o score do benchmark HumanEval - neste momento apenas calcula o pass@1 mas mais tarde vou incluir o pass@10 e pass@100"""
    return_value = None

    # A script do cálculo do score está em human_eval/
    os.chdir("human_eval")

    # Calcula o(s) score(s) do benchmark HumanEval e coloca o resultado num ficheiro de texto    
    os.system(f"python3 evaluate_functional_correctness.py data/samples_{model}.jsonl --problem_file=data/HumanEval.jsonl > human_eval_score.txt")

    # Caso exista o ficheiro, iremos fazer parsing do pass@1, pass@10 e pass@100
    if os.path.exists(f"human_eval_score.txt"):
        with open(f"human_eval_score.txt", 'r') as file:
            # Lê o conteúdo do ficheiro
            lines = file.readlines()

            # Usamos regex para o parsing
            for line in lines:
                match = re.search(r"'pass@1': (\d+\.\d+)", line)
                if match:
                    # Extraimos o valor de pass@1
                    pass_value = match.group(1)
                    return_value = pass_value

    else:
        print(f"Error: The file 'human_eval_score.txt' was not found.")

    # Apagamos o ficheiro de texto temporário
    os.system(f"rm human_eval_score.txt")

    # Voltamos a diretoria inicial
    os.chdir("..")

    # Aqui devolve os scores calculados no parsing (NOTE: no futuro isto irá ser um tuplo do tipo (pass@1, pass@10, pass@100))
    return return_value

def execute_python_script(task_id, prompt, script_to_execute, CSV_FILENAME):
    # Prompt lido do ficheiro JSONL para um ficheiro de texto - resolve o problema do escaping!
    temp_prompt_file = "temp_prompt.txt"
    with open(temp_prompt_file, 'w') as prompt_file:
        prompt_file.write(prompt)

    command = f"python3 {script_to_execute} '{task_id}' {temp_prompt_file} {CSV_FILENAME}"

    os.system(command)


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
        human_eval_score = run_human_eval_benchmark(model_script[:-3])
        add_human_eval_score_in_csv(FILENAME, FILENAME, "HumanEval pass@1", human_eval_score)
    else:
        print("Ficheiro JSONL não pertence a nenhum benchmark considerado")


if __name__ == "__main__":

    # Nome do CSV final
    FILENAME = "measurements.csv"

    os.system("sudo chmod -R a+r /sys/class/powercap/intel-rapl")

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
        print(f"------------------ Executed times = {i+1} ------------------\n")
        for script in scripts_to_execute:
            for prompt_file in prompt_files:
                start_measure(script, prompt_file)