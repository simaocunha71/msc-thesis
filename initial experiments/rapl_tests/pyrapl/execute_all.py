import json
import subprocess
import re
import csv
import os
import shlex

def get_scripts():
    scripts = []
    scripts.append('llama-2-7b.Q2_K.py')
    return scripts

def execute_python_script(task_id, prompt, script_to_execute):
    # NOTE: Assure that scripts name has the correct name of the LLM

    # Quote the script path and prompt to handle spaces and special characters
    script_path = shlex.quote(script_to_execute)
    prompt_escaped = shlex.quote(prompt)

    # Compose the command for executing the Python script
    command = f'python3 {script_path} {prompt_escaped} {task_id} >> {task_id}.J'

    # Execute the command using the shell
    subprocess.run(command, shell=True)

def extract_values(model_name, input_text):
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

    label_match = re.search(r'Label\s*:\s*(\w+)', input_text)
    duration_match = re.search(r'Duration\s*:\s*([\d.]+)\s*us', input_text)
    pkg_match = re.search(r'socket 0\s*:\s*([\d.]+)\s*uJ', input_text)
    dram_match = re.search(r'socket 0\s*:\s*([\d.]+)\s*uJ', input_text)

    if label_match and duration_match and pkg_match and dram_match:
        label = label_match.group(1)
        duration = duration_match.group(1)
        pkg = pkg_match.group(1)
        dram = dram_match.group(1)

        return f'{model_name},{label},{duration},{pkg},{dram}'
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
        lines = file.readlines() #NOTE: Provavelmente terá de ser implementado um readline em vez de termos todas as linhas carregadas em memoria
        for line in lines:
            entry = json.loads(line)

            # Gets the task_id and the prompt text from JSONL file
            task_id = entry.get("task_id", "")
            prompt = entry.get("prompt", "")

            # Gets all the script to run (1 per model)
            scripts_to_execute = get_scripts()

            for script in scripts_to_execute:
                
                # Executes the Python script using the task_id and the prompt
                execute_python_script(task_id.replace("/", "_"), prompt, script)

                # Read measurements file from the previous execution
                with open(f"{task_id.replace('/','_')}.J", 'r') as file:
                    input_text = file.read()

                # Gets all the values to append to the CSV file from a single string
                values_to_add = extract_values(get_model_name(script), input_text)
                if values_to_add:
                    with open(FILENAME, 'a', newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerow(values_to_add.split(','))

    #TODO: Apagar todos os ficheiros .J depois do append para o csv final



if __name__ == "__main__":

    FILENAME = "results_pyrapl.csv"

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