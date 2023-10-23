from llama_cpp import Llama
import sys
import json

def get_output(prompt):

    model_name = "../llama_cpp/models/llama-2-7b.Q2_K.gguf"
    max_tokens = 200

    def create_llama():
        return Llama(model_path=model_name, seed=42)

    llm = create_llama()
    output = llm(prompt=prompt, max_tokens=max_tokens, stop=["Q:"], echo=True)["choices"][0]["text"]
    print(output)
    return output

prompt = sys.argv[1]
get_output(prompt)