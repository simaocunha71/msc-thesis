from data import write_jsonl, read_problems
import sys

# Argumentos de setup
model              = sys.argv[1] # Nome do LLM
label              = sys.argv[2] # Label do prompt
output_got_file    = sys.argv[3] # Ficheiro c/ output gerado pelo LLM em formato string

with open(output_got_file, 'r') as prompt_file:
    output_got = prompt_file.read()

#problems = read_problems(f"data/HumanEval.jsonl") # Leitura dos prompts do benchmark
num_samples_per_task = 1                           # Numero de execuções por prompts

samples = [
    dict(
        task_id=label.replace("_", "/"), 
        completion=output_got
    ) for _ in range(num_samples_per_task)
]

# Escrita das samples num ficheiro jsonl
write_jsonl("data/samples_" + model + ".jsonl", samples, append=True)