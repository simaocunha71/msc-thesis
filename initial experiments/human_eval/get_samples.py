from data import write_jsonl, read_problems
import sys

# Argumentos de setup
model = sys.argv[1]      # Nome do LLM
output_got = sys.argv[2] # Output gerado pelo LLM em formato string

problems = read_problems(f"data/HumanEval.jsonl") # Leitura dos prompts do benchmark
num_samples_per_task = 1                          # Numero de execuções por prompts

# Geração das samples
samples = [
    dict(task_id=task_id, completion=output_got)
    for task_id in problems
    for _ in range(num_samples_per_task)
]

# Escrita das samples num ficheiro jsonl
write_jsonl("data/samples_" + model + ".jsonl", samples)
