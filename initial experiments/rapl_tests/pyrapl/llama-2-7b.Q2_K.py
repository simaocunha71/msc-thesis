#question1 = "Q: What is the capital of England?\nA: London\nQ: What is 1+1?\nA: 2\nQ: What are the names of the planets in the Solar System?\nA: "

from llama_cpp import Llama
import sys
import pyRAPL

#Usage: python3 llama2-python_test.py <prompt> <label>
#Example: python3 llama2-python_test ""Building a website can be done in 10 simple steps:\nStep 1:" "HumanEval/42"

prompt = sys.argv[1]
label = (sys.argv[2]).replace('/','_')

model_name = "../../llama_cpp/models/llama-2-7b.Q2_K.gguf"
max_tokens = 64

pyRAPL.setup()

def create_llama():
    return Llama(model_path=model_name, seed=42)

llm = create_llama()

#with pyRAPL.Measurement(label):
output = llm(prompt=prompt, max_tokens=max_tokens, stop=["Q:"], echo=True)["choices"][0]["text"]
  
print(output)
"""
Descrição das colunas CSV:

label (str) - measurement label
timestamp (float) - measurement's beginning time (expressed in seconds since the epoch)
duration (float) - measurement's duration (in micro seconds)
pkg (Optional[List[float]]) - list of the CPU energy consumption -expressed in micro Joules- (one value for each socket) if None, no CPU energy consumption was recorded
dram (Optional[List[float]]) - list of the RAM energy consumption -expressed in seconds- (one value for each socket) if None, no RAM energy consumption was recorded
"""
