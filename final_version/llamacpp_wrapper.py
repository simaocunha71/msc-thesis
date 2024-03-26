from llama_cpp import Llama
import sys, os, re, csv
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
#NOTE: A variação do max_tokens leva a um maior/menor consumo de energia

 # Linguagem a ser executada no benchmark (argumento opcional)
if len(sys.argv) > 6:
    language = sys.argv[6]
else:
    language = None

########################################################################################################
# Ler o prompt do ficheiro temporário
with open(prompt_file_path, 'r') as prompt_file:
    prompt = prompt_file.read()


# Inicialização do Llama.cpp em Python
llm = Llama(model_path=model_name, seed=42, n_ctx=2048, verbose=False)

measure_utils.print_measure_information(model_name, label)

tracker = OfflineEmissionsTracker(country_iso_code="PRT")
# INÍCIO DA MEDIÇÃO
tracker.start()
output = llm(prompt=prompt, max_tokens=max_tokens, stop=["Q:"], echo=True)["choices"][0]["text"]
tracker.stop()
# FIM DA MEDIÇÃO

#print("-------------------------------")
#print(output)
#print("-------------------------------")

measure_utils.save_output_to_file(output, label, language, "prompts_returned", 
                                  measure_utils.extract_llm_name(model_name), 
                                  "humaneval_x")

measure_utils.generate_samples_humaneval_x(measure_utils.extract_llm_name(model_name), output, 
                                           label, language)

measure_utils.add_measurement_to_csv(FILENAME, measure_utils.extract_llm_name(model_name), 
                                     label, tracker)