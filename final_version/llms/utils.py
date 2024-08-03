import json
from llama_cpp import Llama

def get_llm_family(llm_path):
    # Caminho do ficheiro JSON
    json_file_path = 'supported_models.json'
    
    # Ler o JSON do ficheiro
    with open(json_file_path, 'r') as file:
        llm_data = json.load(file)
    
    # Procurar o caminho fornecido nas listas de cada chave
    for item in llm_data:
        for key, paths in item.items():
            if llm_path in paths:
                return key
    
    # Retorna None se o caminho não for encontrado
    return None

def load_llm(llm_path, n_ctx, seed):
    print("ENTREI AQUI")
    llm_family = get_llm_family(llm_path)
    if(llm_family == "LLAMACPP"):
        llm = Llama(model_path=llm_path, seed=seed, n_ctx=n_ctx, verbose=False)
    
    return llm