import json
from llama_cpp import Llama

def get_llm_family(llm_path: str) -> str:
    """
    Gets the key from the JSON file containing the LLM class defined in 'supported_models.json'.

    Args:
        llm_path (str): Path to the LLM model file.

    Returns:
        str (or None): The key representing the LLM class if found, otherwise None.
    """
    json_file_path = 'supported_models.json'
    
    with open(json_file_path, 'r') as file:
        llm_data = json.load(file)
    
    for item in llm_data:
        for key, paths in item.items():
            if llm_path in paths:
                return key
    
    return None

def load_llm(llm_path: str, n_ctx: int, seed: int) -> Llama:
    """
    Loads the LLM model into memory and returns the corresponding Llama object.

    Args:
        llm_path (str): Path to the LLM model file.
        n_ctx (int): Context size (maximum number of tokens the LLM can process).
        seed (int): Seed for reproducing results.

    Returns:
        Llama (or None): The Llama object with the model loaded. If no matching LLM class is found in the supported models.
    """
    llm_family = get_llm_family(llm_path)
    if llm_family == "LLAMACPP":
        llm = Llama(model_path=llm_path, seed=seed, n_ctx=n_ctx, verbose=False)
        return llm
    
    return None