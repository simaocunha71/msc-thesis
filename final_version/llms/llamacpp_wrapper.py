from llama_cpp import Llama
import sys, os, re, csv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import measure_utils as measure_utils
from codecarbon import OfflineEmissionsTracker

########################################################################################################
######################################      Argumentos de setup     ####################################
########################################################################################################

label              = sys.argv[1]       # Identificador da execução do LLM no ficheiro CSV final
prompt_file_path   = sys.argv[2]       # Path do ficheiro de texto que contém o prompt do ficheiro JSONL
FILENAME           = sys.argv[3]       # Nome do ficheiro CSV final a adicionar o conteúdo (append)
model_name         = sys.argv[4]       # Path do LLM
max_tokens         = int(sys.argv[5])  # Número máximo de tokens a ser usado pelo LLM na resposta
benchmark_type     = sys.argv[6]       # Tipo de benchmark a executar (util para a geração das samples)
n_ctx              = int(sys.argv[7])  # Context Size
seed               = int(sys.argv[8])  # Seed usada para as gerações das LLMs
#NOTE: A variação do max_tokens leva a um maior/menor consumo de energia

 # Linguagem a ser executada no benchmark (argumento opcional)
if len(sys.argv) > 9:
    language = sys.argv[9]
else:
    language = None

########################################################################################################
# Ler o prompt do ficheiro temporário
with open(prompt_file_path, 'r') as prompt_file:
    prompt = prompt_file.read()


# Inicialização do Llama.cpp em Python
llm = Llama(model_path=model_name, seed=seed, n_ctx=n_ctx, verbose=False)

measure_utils.print_measure_information(model_name, label)

tracker = OfflineEmissionsTracker(country_iso_code="PRT")
# INÍCIO DA MEDIÇÃO
tracker.start()
output = llm(prompt=prompt, max_tokens=max_tokens, stop=["Q:"], echo=True)["choices"][0]["text"]
tracker.stop()
# FIM DA MEDIÇÃO

if benchmark_type == "humaneval_x":
    measure_utils.save_output_to_file(output, label, language, "prompts_returned", 
                                  measure_utils.extract_llm_name(model_name), 
                                  "humaneval_x")
    measure_utils.generate_samples_humaneval_x(measure_utils.extract_llm_name(model_name), output, 
                                           label, language)
elif benchmark_type == "mbpp":
    measure_utils.save_output_to_file(output, label, None, "prompts_returned", 
                                  measure_utils.extract_llm_name(model_name), 
                                  "mbpp")
    measure_utils.generate_samples_mbpp(measure_utils.extract_llm_name(model_name), 
                                    output, 
                                    label)

measure_utils.add_measurement_to_csv(FILENAME, measure_utils.extract_llm_name(model_name), 
                                     label, tracker)
