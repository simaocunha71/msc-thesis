#question1 = "Q: What is the capital of England?\nA: London\nQ: What is 1+1?\nA: 2\nQ: What are the names of the planets in the Solar System?\nA: "

from llama_cpp import Llama
import sys, os, subprocess, time, re, csv, shlex
import pyRAPL

#Usage: python3 llama2-python_test.py <prompt> <label>
#Example: python3 llama2-python_test ""Building a website can be done in 10 simple steps:\nStep 1:" "HumanEval/42"


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
with open(prompt_file_path, 'r') as prompt_file:
    prompt = prompt_file.read()

model_name = "llama_cpp/models/llama-2-7b.Q2_K.gguf" # Path do LLM
max_tokens = 512                                     # Número máximo de tokens a ser usado pelo LLM na resposta
#NOTE: A variação do max_tokens leva a um maior/menor consumo de energia

print_measure_information(model_name, label)


# A medição do tempo de execução vai estar em segundos e usamos funções do Python para este cálculo
start_time = time.time()

#os.system(f'sudo RAPL/main "python3 -c \'from llama_cpp import Llama; print(Llama(model_path="llama_cpp/models/llama-2-7b.Q2_K.gguf", seed=42, verbose=False)(prompt="{prompt}", max_tokens=512, stop=["Q:"], echo=True)["choices"][0]["text"])\' > output_generated.txt" 1')

#os.system(f'sudo RAPL/main "./llama_cpp/main -m {model_name} -p "{prompt}" -n {max_tokens} -e 2> {os.devnull} > output_generated.txt" 1')
os.system(f'sudo RAPL/main "./llama_cpp/main -m {model_name} -p \'$(cat {prompt_file_path})\' -n {max_tokens} -e > output_generated.txt" 1 {label.replace("/", "_")}')

end_time = time.time()

execution_time = end_time - start_time

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


# Adição da medição ao ficheiro CSV final
with open(FILENAME, 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    try:
        csv_writer.writerow(["llama-2-7b.Q2_K", label, execution_time, str(1), str(1), str(1), str(1)])
    except:
        csv_writer.writerow(["llama-2-7b.Q2_K", label, execution_time, "ERROR", "ERROR", "ERROR", "ERROR"])


"""
Descrição das colunas CSV:

label (str) - measurement label
timestamp (float) - measurement's beginning time (expressed in seconds since the epoch)
duration (float) - measurement's duration (in micro seconds)
pkg (Optional[List[float]]) - list of the CPU energy consumption -expressed in micro Joules- (one value for each socket) if None, no CPU energy consumption was recorded
dram (Optional[List[float]]) - list of the RAM energy consumption -expressed in seconds- (one value for each socket) if None, no RAM energy consumption was recorded
"""

#sudo RAPL/main "./llama_cpp/main -m llama_cpp/models/llama-2-7b.Q2_K.gguf -p "from typing import List\n\n\ndef has_close_elements(numbers: List[float], threshold: float) -> bool:\n    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than\n    given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True\n    \"\"\"\n" -n 512 -e"