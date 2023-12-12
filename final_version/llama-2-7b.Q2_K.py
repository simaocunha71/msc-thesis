#question1 = "Q: What is the capital of England?\nA: London\nQ: What is 1+1?\nA: 2\nQ: What are the names of the planets in the Solar System?\nA: "

from llama_cpp import Llama
import sys, os, re, csv
from codecarbon import OfflineEmissionsTracker

#Usage: python3 llama2-python_test.py <prompt> <label>
#Example: python3 llama2-python_test ""Building a website can be done in 10 simple steps:\nStep 1:" "HumanEval/42"

def convert_kwh_to_j(value):
    return value * (3.6*(10**6))

def print_measure_information(model_name, prompt_id):
    print("\n\nExecuting:")
    print(f"> Model: {model_name}")
    print(f"> Prompt: {prompt_id}\n")

def generate_samples_humaneval_x(model, output, label, language):
    """Gera o ficheiro das samples deste modelo (Benchmark: HumanEval-X)"""

    label = label.replace("/", "_")

    # As scripts de execução do benchmark vão estar na diretoria do "CodeGeeX/", pelo que é mais fácil ir para essa diretoria
    os.chdir("CodeGeeX")

    temp_prompt_file = "temp_output_prompt.txt"
    with open(temp_prompt_file, 'w') as prompt_file:
        prompt_file.write(output)

    # O ficheiro "completion_content.txt" vai conter apenas o código gerado pelo modelo,
    # excluindo-se a assinatura da função e comentários iniciais
    os.system("grep -vxFf ../temp_prompt.txt temp_output_prompt.txt > completion_content.txt")

    # Executa a script get_samples.py que irá calcular as samples de um dado LLM para a execução do HumanEval
    command = f'python3 get_samples.py {model} "{label}" completion_content.txt {language}'
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

 # Linguagem a ser executada no benchmark (argumento opcional)
if len(sys.argv) > 4:
    language = sys.argv[4]
else:
    language = None

# Ler o prompt do arquivo temporário
with open(prompt_file_path, 'r') as prompt_file:
    prompt = prompt_file.read()

model_name = "llama_c++/models/llama-2-7b.Q2_K.gguf" # Path do LLM
max_tokens = 512                                     # Número máximo de tokens a ser usado pelo LLM na resposta
#NOTE: A variação do max_tokens leva a um maior/menor consumo de energia

def create_llama():
    return Llama(model_path=model_name, seed=42, verbose=False)

llm = create_llama()

print_measure_information(model_name, label)

tracker = OfflineEmissionsTracker(country_iso_code="PRT")
# INÍCIO DA MEDIÇÃO
tracker.start()
output = llm(prompt=prompt, max_tokens=max_tokens, stop=["Q:"], echo=True)["choices"][0]["text"]
tracker.stop()
# FIM DA MEDIÇÃO

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

if language is not None:
    if not os.path.exists(models_outputs_directory + "/" + language):
        os.makedirs(models_outputs_directory)

    # Guardar o código gerado pelo modelo na pasta "prompts_returned/llama-2-7b.Q2_K/[language]/"
    output_file_path = os.path.join(models_outputs_directory + "/" + language, f"{label_for_filename}.py")
else:
    # Guardar o código gerado pelo modelo na pasta "prompts_returned/llama-2-7b.Q2_K/"
    output_file_path = os.path.join(models_outputs_directory, f"{label_for_filename}.py")

with open(output_file_path, "w") as output_file:
    output_file.write(output)

generate_samples_humaneval_x("llama-2-7b.Q2_K", output, label, language)

# Adição da medição ao ficheiro CSV final
with open(FILENAME, 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    try:
        csv_writer.writerow(["llama-2-7b.Q2_K", label, 
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

        csv_writer.writerow(["llama-2-7b.Q2_K", label, "ERROR", "ERROR", "ERROR", "ERROR", "ERROR",
                                                       "ERROR", "ERROR", "ERROR", "ERROR"
                            ])