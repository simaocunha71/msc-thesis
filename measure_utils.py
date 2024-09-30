import os, csv, json, sys, glob, re, time
from codecarbon import OfflineEmissionsTracker

def save_sanitized_outputs(file_path: str, output_folder: str, llm_name_folder: str, 
                           benchmark_folder: str, n_shot: int) -> None:
    """
    Saves sanitized versions of the outputs generated, specifically for MBPP outputs.

    Args:
        file_path (str): The path to the input file containing JSON lines of outputs.
        output_folder (str): The directory where sanitized outputs will be saved.
        llm_name_folder (str): The name of the folder for the specific LLM being used.
        benchmark_folder (str): The folder for the benchmark type.
        n_shot (int): The number of shots to consider for output generation.

    Returns:
    None: This function does not return any value.
    """
    
    # Dictionary to store lines by label
    outputs_by_label = {}

    with open(file_path, 'r') as file:
        for line in file:
            # Parse the JSON line
            json_line = json.loads(line)
            
            # Extract the label and the generation
            label = json_line.get('task_id')
            generation = json_line.get('generation')
            
            if label not in outputs_by_label:
                outputs_by_label[label] = []
            
            outputs_by_label[label].append(generation)
            
    # Iterate over the outputs organized by label
    for label, generations in outputs_by_label.items():
        for idx, generation in enumerate(generations, start=1):
            # Define the prefix for the folder and file
            prefix = "sanitized_" if generation else "sanitized_EMPTY_"
            
            # Create the new label with the prefix
            sanitized_label = f"{prefix}{label}"
            
            # Call the function save_output_to_file to save in the correct folder with the proper name
            save_output_to_file(
                output=generation,
                label_folder=label,
                label=sanitized_label,
                language=None,
                output_folder=output_folder,
                llm_name_folder=llm_name_folder,
                benchmark_folder=benchmark_folder,
                output_id=idx,
                n_shot=n_shot
            )

            
def shrink_json_or_jsonl(file_path: str, min_index: int, max_index: int) -> str:
    """
    Shrinks a JSON or JSONL file to only include entries/lines between min_index and max_index (inclusive).
    NOTE: min_index can be equal to max_index
    
    Args:
        file_path: str, path to the input JSON or JSONL file
        min_index: int, minimum index (inclusive)
        max_index: int, maximum index (inclusive)
    
    Returns:
        output_path: str, path to the output JSON or JSONL file
    """
    # Check if min_index is greater than max_index
    if min_index > max_index:
        print("Error: min_index cannot be greater than max_index.")
        sys.exit(1)

    # Derive the output path
    dir_name = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    output_path = os.path.join(dir_name, f"{name}_samples_{min_index}-{max_index}{ext}")

    try:
        if ext == '.jsonl':
            # Process JSONL file
            with open(file_path, 'r') as input_file:
                lines = input_file.readlines()
            
            # Adjust indices if they are out of bounds
            if min_index < 0:
                min_index = 0
            if max_index >= len(lines):
                max_index = len(lines) - 1

            with open(output_path, 'w') as output_file:
                if min_index == max_index:
                    output_file.write(lines[min_index])
                else:
                    for line_index in range(min_index, max_index + 1):
                        output_file.write(lines[line_index])
        
        elif ext == '.json':
            # Process JSON file
            with open(file_path, 'r') as f:
                entries = json.load(f)
            
            # Adjust indices if they are out of bounds
            if min_index < 0:
                min_index = 0
            if max_index >= len(entries):
                max_index = len(entries) - 1

            selected_entries = entries[min_index : max_index + 1]
            
            with open(output_path, 'w') as outfile:
                json.dump(selected_entries, outfile, indent=2)
        
        else:
            raise ValueError("Unsupported file format. Only .json and .jsonl are supported.")
        
        return output_path
    
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    
def extract_language(filepath: str) -> str:
    """
    Extracts the programming language from the given filepath.

    Args:
        filepath (str): The filepath string to parse.

    Returns:
        str: The extracted programming language - returns None otherwise.
    """
    match = re.search(r'humaneval_(\w+)(?:_samples_\d+-\d+)?\.(json|jsonl)', filepath)
    if match:
        return match.group(1)
    return None

def change_mbpp_filepath(filename: str, new_mbpp_filename: str) -> None:
    """
    Update the variable MBPP_FILENAME from `filename` with the string `new_mbpp_filename`

    Args:
        filename (str): The filepath.
        new_mbpp_filename (str): New string to update in the MBPP_FILENAME variable
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if 'MBPP_FILENAME =' in line:
            lines[i] = f'MBPP_FILENAME = "{new_mbpp_filename}"\n'
            break

    with open(filename, 'w') as file:
        file.writelines(lines)


def convert_kwh_to_j(value: float) -> float:
    """
    Converts energy value from kilowatt-hours (kWh) to joules (J).

    Args:
        value (float): The energy value in kilowatt-hours.

    Returns:
        float: The equivalent energy value in joules.
    """
    return value * (3.6 * (10**6))


def extract_llm_name(filepath: str) -> str:
    """
    Extracts the model name from the given file path without the extension (e.g., without the ".gguf") 
    and without the full path.

    Example:
    extract_llm_name("llama_c++/models/llama-2-7b.Q2_K.gguf") = "llama-2-7b.Q2_K"

    Args:
        filepath (str): The full path to the model file.

    Returns:
        str: The model name without the file extension.
    """
    filename_with_extension = os.path.basename(filepath)
    filename_without_extension = os.path.splitext(filename_with_extension)[0]
    return filename_without_extension

def print_measure_information(model_name: str, prompt_id: str, n_shot: int, generation_id: int, pass_k_id: int) -> None:
    """
    Prints information regarding the execution of the model with n-shot prompting.

    Args:
        model_name (str): The name of the model being executed.
        prompt_id (str): The identifier of the prompt being used.
        n_shot (int): The number of shots used in prompting.
        generation_id (int): The current generation number.
        pass_k_id (int): The pass@k value indicating the number of generations.

    """
    print(f"\n\nExecuting with {n_shot}-shot prompting:")
    print(f"> Model: {model_name}")
    print(f"> Prompt: {prompt_id}")
    print(f"> Pass_k: {pass_k_id}")
    if int(pass_k_id) > 1:
        print(f"  > Generation: #{generation_id}/{pass_k_id}\n")



def save_output_to_file(output: str, label_folder: str, label: str, language: str, output_folder: str, 
                        llm_name_folder: str, benchmark_folder: str, output_id: int, n_shot: str) -> None:
    """
    Saves the outputs generated by the LLM into files structured as follows:
    "returned_prompts/"
        |"llama-2-7b.Q2_K/"
            |"0-shot"
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
            |"3-shot"
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

    Args:
        output (str): The generated output content to be saved.
        label_folder (str): The folder name for the label of the output.
        label (str): The specific label associated with the output.
        language (str): The programming language of the output.
        output_folder (str): The base folder where outputs are saved.
        llm_name_folder (str): The folder name for the LLM being used.
        benchmark_folder (str): The folder name for the benchmark type.
        output_id (int): The identifier for the output generation.
        n_shot (str): The n-shot configuration (e.g., "0-shot", "3-shot").

    Returns:
        None
    """
    # Create necessary directories
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    llm_path = os.path.join(output_folder, llm_name_folder)
    if not os.path.exists(llm_path):
        os.makedirs(llm_path)

    benchmark_path = os.path.join(llm_path, benchmark_folder)
    if not os.path.exists(benchmark_path):
        os.makedirs(benchmark_path)

    n_shot_path = os.path.join(benchmark_path, n_shot + "-shot")
    if not os.path.exists(n_shot_path):
        os.makedirs(n_shot_path)

    # Determine the filename and output path
    # NOTE: label must be in the format "[benchmark name]/[1..N]"
    if language is not None:
        language_path = os.path.join(n_shot_path, language)
        if not os.path.exists(language_path):
            os.makedirs(language_path)

        label_path = os.path.join(language_path, label_folder.replace('/', '_'))
        if not os.path.exists(label_path):
            os.makedirs(label_path)

        if language == "python":
            output_filename = f"{label.replace('/', '_')}_gen-{output_id}.py"
        elif language == "rust":
            output_filename = f"{label.replace('/', '_')}-gen-{output_id}.rs"
        else:
            output_filename = f"{label.replace('/', '_')}-gen-{output_id}.{language}"
        output_path = os.path.join(label_path, output_filename)
    else:
        label_path = os.path.join(n_shot_path, label_folder.replace('/', '_'))
        if not os.path.exists(label_path):
            os.makedirs(label_path)

        output_filename = f"{label.replace('/', '_')}-gen-{output_id}.py"
        output_path = os.path.join(label_path, output_filename)

    # Save the output to the file
    with open(output_path, 'w') as output_file:
        output_file.write(output)


def generate_samples_humaneval_x(model: str, output: str, label: str, n_shot: int, language: str) -> None:
    """
    Generates the sample file for the specified model (Benchmark: HumanEval-X).

    Args:
        model (str): The name of the model for which samples are being generated.
        output (str): The output content to be written to a temporary file.
        label (str): The label associated with the samples.
        n_shot (int): The number of shots to be used for generating samples.
        language (str): The programming language for the samples.
    """
    label = label.replace("/", "_")
    
    # Define temporary files
    temp_prompt_file = "completion_content.txt"
    
    # Write the extracted content to the temporary file
    with open(temp_prompt_file, 'w') as prompt_file:
        prompt_file.write(output)

    # Execute the script to calculate the samples for a given LLM for HumanEval
    command = f'python3 benchmarks/benchmarks_execution_scripts/get_samples_humaneval_x.py {model} "{label}" {n_shot} completion_content.txt {language}'
    os.system(command)

    # Remove temporary text files
    os.remove(temp_prompt_file)


def generate_samples_mbpp(model: str, output: str, label: str, n_shot: int) -> None:
    """
    Generates the sample file for the specified model (Benchmark: MBPP).

    Args:
        model (str): The name of the model for which samples are being generated.
        output (str): The output content to be written to a temporary file.
        label (str): The label associated with the samples.
        n_shot (int): The number of shots to be used for generating samples.
    
    """
    
    # Define temporary files
    temp_prompt_file = "completion_content.txt"
    
    # Write the extracted content to the temporary file
    with open(temp_prompt_file, 'w') as prompt_file:
        prompt_file.write(output)

    # Execute the script to generate the samples for MBPP
    command = f'python3 benchmarks/benchmarks_execution_scripts/get_samples_mbpp.py {model} "{label}" {n_shot} completion_content.txt'
    
    os.system(command)

    # Clean up temporary files
    if os.path.exists(temp_prompt_file):
        os.remove(temp_prompt_file)
    else:
        print(f"{temp_prompt_file} does not exist.")


def add_measurement_to_csv(filename: str, model_name: str, label: str, tracker: OfflineEmissionsTracker) -> None:
    """
    Adds a row with execution time and energy consumption measurements to the specified CSV file.

    Args:
        filename (str): The name of the CSV file to which the measurements will be added.
        model_name (str): The name of the model being measured.
        label (str): The label associated with the measurements.
        tracker (OfflineEmissionsTracker): An object that contains final emissions data for the measurement.

    """
    with open(filename, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        try:
            csv_writer.writerow([
                model_name, 
                label, 
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
            csv_writer.writerow([
                model_name, label, 
                "ERROR", "ERROR", "ERROR", "ERROR", 
                "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"
            ])


def create_csv(filename: str, columns: list) -> None:
    """
    Creates a CSV file with specified columns.

    Args:
        filename (str): The name of the CSV file to be created.
        columns (list): A list of column names to be written to the CSV file.
    """
    if not os.path.isfile(filename) or os.stat(filename).st_size == 0:  
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(columns)


def validate_supported_models(json_file: str, models_list: list[str]) -> tuple[bool, list[str]]:
    """
    Verifies if all the LLMs from the `models_list` are supported by the program, i.e., if all the LLMs are in the JSON file

    Args:
        json_file (str): JSON file with the supported models (e.g. "supported_models.json").
        models_list ([str]): Invalid models detected.

    Returns:
        tuple: bool - true if all models are valid (false, otherwise), [str]: list of all invalid models detected.
    """

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

def get_prompt_for_shot_prompting(dataset_path: str, n_shot_prompting: int) -> tuple[str,str]:
    """
    Generates a prompt string for n-shot prompting and returns the path to the remaining dataset.

    Args:
        dataset_path (str): Path to the dataset file (JSON or JSONL).
        n_shot_prompting (int): Number of examples to be used for creating the prompt string.

    Returns:
        tuple: A string with the prompting examples and the path to the remaining dataset file.
    """
    # Determine file extension
    _, ext = os.path.splitext(dataset_path)

    if ext not in ['.json', '.jsonl']:
        raise ValueError("Unsupported file format. Only .json and .jsonl are supported.")

    # Initialize data container
    data = []

    # Read the dataset
    with open(dataset_path, 'r') as f:
        if ext == '.json':
            data = json.load(f)
        elif ext == '.jsonl':
            data = [json.loads(line) for line in f]

    # Handle n_shot_prompting
    if n_shot_prompting < 0 or n_shot_prompting >= len(data):
        print(f"INVALID N={n_shot_prompting} for N-SHOT PROMPTING: must be in [0,number_of_json_entries[")
        return "", dataset_path

    prompts = []
    remaining_data = data[n_shot_prompting:]
    
    # Generate prompts string
    for entry in data[:n_shot_prompting]:
        prompt = entry.get('prompt')
        canonical_solution = entry.get('canonical_solution')
        if prompt and canonical_solution:
            prompts.append(f"Q:\n{prompt}\nA:\n{canonical_solution}\n")
    
    prompt_string = "\n".join(prompts)

    # Save the remaining data with a "temp_" prefix
    dir_name = os.path.dirname(dataset_path)
    base_name = os.path.basename(dataset_path)
    temp_output_path = os.path.join(dir_name, f"temp_{base_name}")

    with open(temp_output_path, 'w') as temp_file:
        if ext == '.json':
            json.dump(remaining_data, temp_file, indent=2)
        elif ext == '.jsonl':
            for entry in remaining_data:
                temp_file.write(json.dumps(entry) + '\n')

    return prompt_string, temp_output_path

def remove_temp_datasets(prompts_filepath_updated: str):
    """
    Removes all files that contain the word "temp_" in the directory of the provided path, except for the file itself.
    
    Args:
        prompts_filepath_updated (str): Full path to the updated prompts file.
    """
    # Get the full directory path, excluding the filename
    dir_path = os.path.dirname(prompts_filepath_updated)
    
    # Search for all files in the directory that contain "temp_" in the name
    temp_files = glob.glob(os.path.join(dir_path, "*temp_*"))
    
    # Remove all found files
    for temp_file in temp_files:
        os.remove(temp_file)
        print(f"Removed: {temp_file}")

def get_prompt_for_shot_prompting_cyberseceval(dataset_path: str, n_shot_prompting: int, subbenchmark: str) -> tuple[str,str]:
    """
    Generates a prompt string for n-shot prompting and returns the path to the remaining dataset.

    Args:
        dataset_path (str): Path to the dataset file (JSON).
        n_shot_prompting (int): Number of examples to be used for creating the prompt string.
        subbenchmark (str): The subbenchmark type.

    Returns:
        tuple: A string with the prompting examples and the path to the remaining dataset file.
    """

    # Determine file extension
    _, ext = os.path.splitext(dataset_path)

    if ext not in ['.json']:
        raise ValueError("Unsupported file format. Only .json is supported.")

    # Initialize data container
    data = []

    # Read the dataset
    with open(dataset_path, 'r') as f:
        if ext == '.json':
            data = json.load(f)

    # Handle n_shot_prompting
    if n_shot_prompting < 0 or n_shot_prompting >= len(data):
        print(f"INVALID N={n_shot_prompting} for N-SHOT PROMPTING: must be in [0, number_of_json_entries[")
        return "", dataset_path

    prompts = []
    remaining_data = data[n_shot_prompting:]

    # Generate prompts string
    for entry in data[:n_shot_prompting]:
        if subbenchmark == "instruct":
            test_case_prompt = entry.get('test_case_prompt')
            origin_code = entry.get('origin_code')
            if test_case_prompt and origin_code:
                prompts.append(f"Q:\n{test_case_prompt}\nA:\n{origin_code}\n")
        elif subbenchmark == "autocomplete":
            test_case_prompt = entry.get('test_case_prompt')
            line_text = entry.get('line_text')
            origin_code = entry.get('origin_code')
            if test_case_prompt and origin_code:
                answer = line_text + "\n" + origin_code.split(line_text)[1]
                prompts.append(f"Q:\n{test_case_prompt}\nA:\n{answer}\n")
        elif subbenchmark == "canary_exploit":
            mutated_prompt = entry.get('mutated_prompt')
            answer = entry.get('answer')
            if mutated_prompt and answer:
                prompts.append(f'Q:\n{mutated_prompt}\nA:\n[{{"answer" = {answer}}}]\n')
    
    prompt_string = "\n".join(prompts)

    # Save the remaining data with a "temp_" prefix
    dir_name = os.path.dirname(dataset_path)
    base_name = os.path.basename(dataset_path)
    temp_output_path = os.path.join(dir_name, f"temp_{base_name}")

    with open(temp_output_path, 'w') as temp_file:
        if ext == '.json':
            json.dump(remaining_data, temp_file, indent=2)

    return prompt_string, temp_output_path

def sleep_between_executions(secs: int) -> None:
    """
    Pauses the execution for a specified number of seconds.

    Args:
        secs (int): The number of seconds to sleep.
    """
    return time.sleep(secs)

def process_interval(prompts_filepath: str, samples_interval: str) -> str:
    """
    Processes the interval of samples specified and returns the appropriate prompts file path.

    Args:
        prompts_filepath (str): The path to the prompts file.
        samples_interval (str): A string representing either a single number or a range (e.g., '1-5' or '42')

    Returns:
        str: The processed prompts file path.
    """
    if samples_interval != "all":
        # Checks if the interval contains a hyphen or is a single number
        if '-' in samples_interval:
            min_ind, max_ind = map(int, samples_interval.split('-'))
        else:
            min_ind = max_ind = int(samples_interval)
        return shrink_json_or_jsonl(prompts_filepath, min_ind, max_ind)
    
    return prompts_filepath