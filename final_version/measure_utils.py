import os, csv, json

def change_max_tokens_value(filename, new_max_tolens):
    """Substitui o valor de max_tokens vindo do ArgumentParser no ficheiro .py do CyberSecEval (i.e. llm.py)"""
    with open(filename, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if 'MAX_TOKENS =' in line:
            lines[i] = f'MAX_TOKENS = {new_max_tolens}\n'
            break

    with open(filename, 'w') as file:
        file.writelines(lines)

def convert_kwh_to_j(value):
    return value * (3.6*(10**6))

def extract_llm_name(filepath):
    """
    Devolve o nome do modelo sem a extensão (e.g. sem o ".gguf") e sem o path completo
    Ex: extract_llm_name("llama_c++/models/llama-2-7b.Q2_K.gguf") = "llama-2-7b.Q2_K" 
    """
    filename_with_extension = os.path.basename(filepath)
    filename_without_extension = os.path.splitext(filename_with_extension)[0]
    return filename_without_extension

def print_measure_information(model_name, prompt_id):
    print("\n\nExecuting:")
    print(f"> Model: {model_name}")
    print(f"> Prompt: {prompt_id}\n")

def save_output_to_file(output, label, language, output_folder, llama_folder, language_folder):
    """
    Guarda os outputs gerados pelo LLM em ficheiros cujo file system é o seguinte:
    "prompts_returned/"
        |"llama-2-7b.Q2_K/"
            |"humaneval_x/"
                |"CPP_0.cpp"
                |"CPP_1.cpp"
                |"CPP_2.cpp"
                |...
                |"Go_0.go"
                |...
                |"Python_163.py"
            |"cyberseceval/"
                |TBD
        |"llama-2-7b.Q3_K_L/"
            |TBD
    """
    # Criar diretórios necessários
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    llama_path = os.path.join(output_folder, llama_folder)
    if not os.path.exists(llama_path):
        os.makedirs(llama_path)

    if language is not None:
        language_path = os.path.join(llama_path, language_folder)
        if not os.path.exists(language_path):
            os.makedirs(language_path)

    # Determinar o nome do ficheiro e o caminho de saída
    if language is not None:
        if language == "python":
            output_filename = f"{label.replace('/', '_')}.py"
        else:
            output_filename = f"{label.replace('/', '_')}.{language}"
        output_path = os.path.join(language_path, output_filename)
    else:
        output_filename = f"{label}.txt"
        output_path = os.path.join(llama_path, output_filename)

    # Salvar o output no ficheiro
    with open(output_path, 'w') as output_file:
        output_file.write(output)

def generate_samples_humaneval_x(model, output, label, language):
    """Gera o ficheiro das samples deste modelo (Benchmark: HumanEval-X)"""

    label = label.replace("/", "_")

    temp_prompt_file = "temp_output_prompt.txt"
    with open(temp_prompt_file, 'w') as prompt_file:
        prompt_file.write(output)

    # O ficheiro "completion_content.txt" vai conter apenas o código gerado pelo modelo,
    # excluindo-se a assinatura da função e comentários iniciais
    os.system("grep -vxFf temp_prompt.txt temp_output_prompt.txt > completion_content.txt")

    # Executa a script get_samples.py que irá calcular as samples de um dado LLM para a execução do HumanEval
    command = f'python3 benchmarks_execution_scripts/get_samples_humaneval_x.py {model} "{label}" completion_content.txt {language}'
    os.system(command)

    # Remove os ficheiros de texto temporários
    os.remove(temp_prompt_file)
    os.remove("completion_content.txt")
    os.remove("temp_prompt.txt")

def add_measurement_to_csv(FILENAME, model_name, label, tracker):
    """ Adiciona uma linha com as medições de tempos de execução e de energia consumida ao ficheiro CSV """

    with open(FILENAME, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        try:
            csv_writer.writerow([model_name, label, 
                                    tracker.final_emissions_data.duration, 
                                    convert_kwh_to_j(tracker.final_emissions_data.cpu_energy), 
                                    convert_kwh_to_j(tracker.final_emissions_data.ram_energy), 
                                    convert_kwh_to_j(tracker.final_emissions_data.gpu_energy),  
                                    tracker.final_emissions_data.cpu_power, 
                                    tracker.final_emissions_data.ram_power,  
                                    tracker.final_emissions_data.gpu_power, 
                                    tracker.final_emissions_data.emissions,
                                    tracker.final_emissions_data.emissions_rate
                                ])
        except Exception as e:
            print("------------------------------------------")
            print(e)
            print("------------------------------------------")
            csv_writer.writerow([model_name, label, "ERROR", "ERROR", "ERROR", "ERROR", "ERROR",
                                                    "ERROR", "ERROR", "ERROR", "ERROR"
                                ])

def create_csv(filename, columns):
    """Cria um ficheiro csv com umas colunas específicas"""
    if not os.path.isfile(filename) or os.stat(filename).st_size == 0:  
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(columns)

def validate_supported_models(json_file, models_list):
    """Verifica se uma string de paths de LLMs estão suportados pelo programa, lendo o ficheiro JSON de modelos s"""
    invalid_models = []
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

            json_strings = [value for sublist in data for value in sublist.values()]
            json_models = [item for sublist in json_strings for item in sublist]

            for string in models_list:
                if string not in json_models:
                    invalid_models.append(string)
            if invalid_models:
                return False, invalid_models
            else:
                return True, []
    except FileNotFoundError:
        print(f"The file '{json_file}' was not found.")