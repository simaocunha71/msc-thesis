from data import write_jsonl, read_problems
import sys

# Argumentos de setup
model              = sys.argv[1] # Nome do LLM
label              = sys.argv[2] # Label do prompt
output_got         = sys.argv[3] # Output gerado pelo LLM em formato string
entry_point        = sys.argv[4] # Nome da função (originária do ficheiro dos prompts)
canonical_solution = sys.argv[5] # Solução esperada (originária do ficheiro dos prompts)
test               = sys.argv[6] # Conjunto de testes da função (originária do ficheiro dos prompts)

#problems = read_problems(f"data/HumanEval.jsonl") # Leitura dos prompts do benchmark
num_samples_per_task = 1                           # Numero de execuções por prompts

samples = [
    dict(
        task_id=label.replace("_", "/"), 
        completion=output_got.replace(r'\n', '\n').replace(r'\"', '"').replace(r"\'", "'").replace(r'\>', '>').replace(r'\<', '<').replace(r'\n', '\n').replace(r'\<', '<').replace(r'\>', '>').replace(r"\'", "'").replace(r'\"', '"')
    ) for _ in range(num_samples_per_task)
]

# Escrita das samples num ficheiro jsonl
write_jsonl("data/samples_" + model + ".jsonl", samples, append=True)
