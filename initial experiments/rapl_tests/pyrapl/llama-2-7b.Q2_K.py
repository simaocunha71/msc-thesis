#question1 = "Q: What is the capital of England?\nA: London\nQ: What is 1+1?\nA: 2\nQ: What are the names of the planets in the Solar System?\nA: "

from llama_cpp import Llama
import sys, os, subprocess, time, re, csv
import pyRAPL

#Usage: python3 llama2-python_test.py <prompt> <label>
#Example: python3 llama2-python_test ""Building a website can be done in 10 simple steps:\nStep 1:" "HumanEval/42"

def run_human_eval_benchmark(model, output):
    """Calcula o score do benchmark HumanEval - neste momento apenas calcula o pass@1 mas mais tarde vou incluir o pass@10 e pass@100"""
    return_value = None

    # As scripts de execução do benchmark vão estar na diretoria do "human_eval/", pelo que é mais fácil ir para essa diretoria
    os.chdir("../../human_eval")

    # Executa a script get_samples.py que irá calcular as samples de um dado LLM para a execução do HumanEval
    command = f'python3 get_samples.py {model} "{output}"'
    subprocess.run(command,  shell=True)

    # Calcula o(s) score(s) do benchmark HumanEval e coloca o resultado num ficheiro de texto    
    subprocess.run(f"python3 evaluate_functional_correctness.py data/samples_{model}.jsonl --problem_file=data/HumanEval.jsonl > human_eval_score.txt", shell=True)

    # Caso exista o ficheiro, iremos fazer parsing do pass@1, pass@10 e pass@100
    if os.path.exists("human_eval_score.txt"):
        with open("human_eval_score.txt", 'r') as file:
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

    # Apagamos o ficheiro de texto
    subprocess.run("rm human_eval_score.txt", shell=True)
    
    # Voltamos à diretoria inicial
    os.chdir("../rapl_tests/pyrapl")
    
    # Aqui devolve os scores calculados no parsing (NOTE: no futuro isto irá ser um tuplo do tipo (pass@1, pass@10, pass@100))
    return return_value


# Argumentos da função e setup

prompt     = sys.argv[1]  # Prompt a ser usado pelo LLM
label      = sys.argv[2]  # Identificador da execução do LLM no ficheiro CSV final
FILENAME   = sys.argv[3]  # Nome do ficheiro CSV final a adicionar o conteúdo (append)

model_name = "../../llama_cpp/models/llama-2-7b.Q2_K.gguf" #Path do LLM
max_tokens = 500          # Número máximo de tokens a ser usado pelo LLM na resposta
#NOTE: A variação do max_tokens leva a um maior/menor consumo de energia

pyRAPL.setup()

def create_llama():
    return Llama(model_path=model_name, seed=42)

llm = create_llama()

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

human_eval_score = run_human_eval_benchmark("llama-2-7b.Q2_K", output.replace('"', r'\"').replace("'", r"\'").replace(">", r"\>").replace("<", r"\<").replace("\n", r'\n'))

# Adição da medição ao ficheiro CSV final
with open(FILENAME, 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    #NOTE: colocar em J e em S
    csv_writer.writerow(["llama-2-7b.Q2_K", label, execution_time, measure.result.pkg[0], measure.result.dram[0], human_eval_score])

"""
Descrição das colunas CSV:

label (str) - measurement label
timestamp (float) - measurement's beginning time (expressed in seconds since the epoch)
duration (float) - measurement's duration (in micro seconds)
pkg (Optional[List[float]]) - list of the CPU energy consumption -expressed in micro Joules- (one value for each socket) if None, no CPU energy consumption was recorded
dram (Optional[List[float]]) - list of the RAM energy consumption -expressed in seconds- (one value for each socket) if None, no RAM energy consumption was recorded
"""