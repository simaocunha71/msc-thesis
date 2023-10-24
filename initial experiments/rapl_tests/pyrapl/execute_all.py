import json
import subprocess
import re
import csv
import os
import shlex
import time

def transform_to_base_unit(value):
    return str(float(value) * 10**-6)

def get_scripts():
    scripts = []
    scripts.append('llama-2-7b.Q2_K.py')
    return scripts

def get_humal_eval_score(model):
    #Para já apenas vai devolver o pass@1, mas depois vai devolver um tuplo com o pass@10 e pass@100
    #TODO: 
    # executar o get_samples.py
    # executar "python3 evaluate_functional_correctness.py data/samples_llama-2-7b.Q2_K.jsonl --problem_file=data/problems_llama-2-7b.Q2_K.jsonl" usando o nome do modelo e redirecionar para um ficheiro de texto
    # usar regex para dar parse do pass@1 (mais tarde do pass@10 e pass@100) 
    # apagar esse ficheiro de texto
    # retornar o valor de pass@1 (mais tarde um tuplo incluindo o pass@10 e pass@100)
    pass

def execute_python_script(task_id, prompt, script_to_execute):
    # NOTE: Assure that scripts name has the correct name of the LLM

    # Quote the script path and prompt to handle spaces and special characters
    script_path = shlex.quote(script_to_execute)
    prompt_escaped = shlex.quote(prompt)

    # Compose the command for executing the Python script
    command = f'python3 {script_path} {prompt_escaped} {task_id} > {task_id}.J'

    # Execute the command using the shell
    subprocess.run(command, shell=True)


def extract_values(model_name, input_text, execution_time):
    # Regular expressions for each value
    # Output file content example to parse
    """
    Label : HumanEval/42
    Begin : Sun Oct  8 19:19:00 2023
    Duration : 15923350.7570 us
    -------------------------------
    PKG :
        socket 0 :  961007123.0000 uJ
    -------------------------------
    DRAM :
        socket 0 :  40850237.0000 uJ
    -------------------------------
    """

    humal_eval_score = get_humal_eval_score(model_name)

    label_match = re.search(r'Label\s*:\s*(\w+)', input_text)
    pkg_match = re.search(r'\bPKG\s*:\s*socket 0\s*:\s*([\d.]+)\s*uJ', input_text)
    dram_match = re.search(r'\bDRAM\s*:\s*socket 0\s*:\s*([\d.]+)\s*uJ', input_text)

    if label_match and pkg_match and dram_match:
        label = label_match.group(1)
        pkg = pkg_match.group(1)
        dram = dram_match.group(1)

        #NOTE: para já apenas vou por pass@1, mas tenho de dar append ao pass@10 e pass@100 - criar tantas funções quantos os pass
        return f'{model_name},{label},{execution_time},{transform_to_base_unit(pkg)},{transform_to_base_unit(dram), {humal_eval_score}}'
    else:
        return None

def get_model_name(script_path):
    """Get the LLM name using the script's filename"""
    result = re.match(r'^(.*?)(\.py)', script_path)
    if result:
        return result.group(1)
    else:
        return None

def start_measure(prompts_filepath):
    with open(prompts_filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            entry = json.loads(line)

            task_id = entry.get("task_id", "")
            prompt = entry.get("prompt", "")

            scripts_to_execute = get_scripts()

            for script in scripts_to_execute:
                # Measure execution time
                start_time = time.time()

                execute_python_script(task_id.replace("/", "_"), prompt, script)

                end_time = time.time()
                execution_time = end_time - start_time

                with open(f"{task_id.replace('/', '_')}.J", 'r') as file:
                    input_text = file.read()

                values_to_add = extract_values(get_model_name(script), input_text, execution_time)
                if values_to_add:

                    with open(FILENAME, 'a', newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerow(values_to_add.split(','))

    subprocess.run("sudo rm *.J", shell=True)


if __name__ == "__main__":

    FILENAME = "results_pyrapl.csv"

    subprocess.run("sudo chmod -R a+r /sys/class/powercap/intel-rapl", shell=True)

    # List with the values of the csv's header
    header_list = [
                   "LLM",
                   "Benchmark prompt",
                   "Execution time",
                   "Package",
                   "DRAM"
                  ]

    if not os.path.isfile(FILENAME) or os.stat(FILENAME).st_size == 0:
        # If file doesn't exists, it will be created
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header_list)

    start_measure('prompts.jsonl')