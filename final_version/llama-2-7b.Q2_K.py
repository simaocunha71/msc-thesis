#question1 = "Q: What is the capital of England?\nA: London\nQ: What is 1+1?\nA: 2\nQ: What are the names of the planets in the Solar System?\nA: "

from llama_cpp import Llama
import sys, os, subprocess, time, re, csv, shlex
import pyRAPL

#Usage: python3 llama2-python_test.py <prompt> <label>
#Example: python3 llama2-python_test ""Building a website can be done in 10 simple steps:\nStep 1:" "HumanEval/42"

def print_measure_information(model_name, prompt_id):
    print(f"\n\nModel: {model_name}")
    print(f"Prompt: {prompt_id}\n")

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
    subprocess.run(f"python3 evaluate_functional_correctness.py data/samples_{model}.jsonl --problem_file=data/HumanEval.jsonl > human_eval_score.txt", shell=True)

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
    subprocess.run(f"rm human_eval_score.txt", shell=True)

    # Voltamos a diretoria inicial
    os.chdir("..")

    # Aqui devolve os scores calculados no parsing (NOTE: no futuro isto irá ser um tuplo do tipo (pass@1, pass@10, pass@100))
    return return_value


def generate_samples(model, output, label):
    """Gera o ficheiro das samples deste modelo"""

    label = label.replace("/", "_")

    # As scripts de execução do benchmark vão estar na diretoria do "human_eval/", pelo que é mais fácil ir para essa diretoria
    os.chdir("human_eval")

    temp_prompt_file = "temp_output_prompt.txt"
    with open(temp_prompt_file, 'w') as prompt_file:
        prompt_file.write(output)

    # O ficheiro "completion_content.txt" vai conter apenas o código gerado pelo modelo,
    # excluindo-se a assinatura da função e comentários iniciais
    subprocess.run("grep -vxFf ../temp_prompt.txt temp_output_prompt.txt > completion_content.txt", shell=True)

    # Executa a script get_samples.py que irá calcular as samples de um dado LLM para a execução do HumanEval
    command = f'python3 get_samples.py {model} "{label}" completion_content.txt'
    subprocess.run(command,  shell=True)

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

pyRAPL.setup()

def create_llama():
    return Llama(model_path=model_name, seed=42, verbose=False)

llm = create_llama()

print_measure_information(model_name, label)

pyRAPL.setup()

# A medição do tempo de execução vai estar em segundos e usamos funções do Python para este cálculo
start_time = time.time()

# INÍCIO DA MEDIÇÃO
measure = pyRAPL.Measurement('llama-2-7b.Q2_K')
measure.begin()
output = llm(prompt=prompt, max_tokens=max_tokens, stop=["Q:"], echo=True)["choices"][0]["text"]
measure.end()
# FIM DA MEDIÇÃO

end_time = time.time()

execution_time = end_time - start_time

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
    #NOTE: colocar em J e em S
    csv_writer.writerow(["llama-2-7b.Q2_K", label, execution_time, measure.result.pkg[0], measure.result.dram[0]])

human_eval_score = run_human_eval_benchmark("llama-2-7b.Q2_K")
add_human_eval_score_in_csv(FILENAME, FILENAME, "HumanEval pass@1", human_eval_score)
"""
Descrição das colunas CSV:

label (str) - measurement label
timestamp (float) - measurement's beginning time (expressed in seconds since the epoch)
duration (float) - measurement's duration (in micro seconds)
pkg (Optional[List[float]]) - list of the CPU energy consumption -expressed in micro Joules- (one value for each socket) if None, no CPU energy consumption was recorded
dram (Optional[List[float]]) - list of the RAM energy consumption -expressed in seconds- (one value for each socket) if None, no RAM energy consumption was recorded
"""