import sys, os, subprocess, time, re, csv

def read_values_from_Jfile(file_path):
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            package = float(row["Package"])
            core = float(row["Core"])
            gpu = float(row["GPU"])
            dram = float(row["DRAM"])
            time = float(row["Time"])
            
            # Returning a tuple with the values
            values_tuple = package, core, gpu, dram, time
            
            # Remove the file after reading values
            os.remove(file_path)
            
            return values_tuple

def print_measure_information(model_name, prompt_id):
    print("\n\nExecuting:")
    print(f"> Model: {model_name}")
    print(f"> Prompt: {prompt_id}\n")

def generate_samples(model, output, label):
    """Gera o ficheiro das samples deste modelo (Benchmark: HumanEval)"""

    label = label.replace("/", "_")

    # As scripts de execução do benchmark vão estar na diretoria do "human_eval/", pelo que é mais fácil ir para essa diretoria
    os.chdir("human_eval")

    temp_prompt_file = "temp_output_prompt.txt"
    with open(temp_prompt_file, 'w') as prompt_file:
        prompt_file.write(output)

    # O ficheiro "completion_content.txt" vai conter apenas o código gerado pelo modelo,
    # excluindo-se a assinatura da função e comentários iniciais
    os.system("grep -vxFf ../temp_prompt.txt temp_output_prompt.txt > completion_content.txt")

    # Executa a script get_samples.py que irá calcular as samples de um dado LLM para a execução do HumanEval
    command = f'python3 get_samples.py {model} "{label}" completion_content.txt'
    os.system(command)

    # Remove os ficheiros de texto temporários
    os.remove(temp_prompt_file)
    os.remove("completion_content.txt")
    os.remove("../temp_prompt.txt")
    
    # Voltamos à diretoria inicial
    os.chdir("..")

# Argumentos da função e setup
label              = sys.argv[1]  # Identificador da execução do LLM no ficheiro CSV final
prompt_file_path   = sys.argv[2]  # Path do ficheiro de texto que contém o prompt do ficheiro JSONL
FILENAME           = sys.argv[3]  # Nome do ficheiro CSV final a adicionar o conteúdo (append)

# Ler o prompt do arquivo temporário
#with open(prompt_file_path, 'r') as prompt_file:
#    prompt = prompt_file.read()

model_name = "llama_c++/models/llama-2-7b.Q2_K.gguf" # Path do LLM
max_tokens = 512                                     # Número máximo de tokens a ser usado pelo LLM na resposta
#NOTE: A variação do max_tokens leva a um maior/menor consumo de energia

print_measure_information(model_name, label)

#python_code = f"from llama_cpp import Llama; with open('{prompt_file_path}', 'r') as f: prompt = f.read(); model_name = '{model_name}'; max_tokens = {max_tokens}; output = Llama(model_path=model_name, seed=42, verbose=False)(prompt=prompt, max_tokens=max_tokens, stop=['Q:'], echo=True)['choices'][0]['text']; print(output)"

python_code = '''\
#!/usr/bin/env python3
import sys
sys.path.append("/home/simao/.local/lib/python3.10/site-packages")
from llama_cpp import Llama

with open('{}', 'r') as prompt_file:
    prompt = prompt_file.read()

output = Llama(model_path='{}', seed=42, verbose=False)(prompt=prompt, max_tokens={}, stop=['Q:'], echo=True)['choices'][0]['text']

with open('output_generated.txt', 'w') as output_file:
    output_file.write(output)
'''.format(prompt_file_path, model_name, max_tokens)

temporary_script = "temp_script.py"

# Cria um arquivo temporário para armazenar o código Python
with open(temporary_script, 'w') as script_file:
    script_file.write(python_code)

# Executa o script Python usando o comando shell
os.system(f'chmod +x {temporary_script}')

command = f'sudo RAPL/main "python3 {temporary_script}" 1 {label.replace("/", "_")}'
os.system(command)

# Remove o arquivo temporário
os.remove('temp_script.py')

#command = f'sudo RAPL/main "./llama_cpp/main -m {model_name} -p \'$(cat {prompt_file_path})\' -n {max_tokens} -e --log-disable > output_generated.txt" 1 {label.replace("/", "_")} 2>/dev/null'

# Output lido do ficheiro de texto temporário
with open("output_generated.txt", "r") as file:
    output = file.read()

# Criar a pasta "prompts_returned" se não existir
outputs_directory = "prompts_returned"
if not os.path.exists(outputs_directory):
    os.makedirs(outputs_directory)

# Substituir '/' por '_' no nome do ficheiro
label_for_filename = label.replace("/", "_")

# Criar a pasta "llama-2-7b.Q2_K/" se não existir
models_outputs_directory = outputs_directory + "/" + ''.join(model_name.split('/')[-1].split('.')[:-1])
if not os.path.exists(models_outputs_directory):
    os.makedirs(models_outputs_directory)

# Guardar o código gerado pelo modelo na pasta "prompts_returned/llama-2-7b.Q2_K/"
output_file_path = os.path.join(models_outputs_directory, f"{label_for_filename}.py")
with open(output_file_path, "w") as output_file:
    output_file.write(output)

generate_samples("llama-2-7b.Q2_K", output, label)

package, core, gpu, dram, time = read_values_from_Jfile(label.replace("/", "_") + ".J")

# Adição da medição ao ficheiro CSV final
with open(FILENAME, 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    try:
        csv_writer.writerow(["llama-2-7b.Q2_K", label, time, package, core, gpu, dram])
    except:
        csv_writer.writerow(["llama-2-7b.Q2_K", label, "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"])