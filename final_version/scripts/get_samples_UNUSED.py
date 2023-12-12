import gzip
import json
import os
from typing import Iterable, Dict
import sys

def write_jsonl(filename: str, data: Iterable[Dict], append: bool = False):
    """
    Writes an iterable of dictionaries to jsonl
    """
    mode = 'a' if append else 'w'
    filename = os.path.expanduser(filename)
    if filename.endswith(".gz"):
        with gzip.open(filename, mode, encoding='utf-8') as gzfp:
            for x in data:
                gzfp.write(json.dumps(x) + "\n")
    else:
        with open(filename, mode, encoding='utf-8') as fp:
            for x in data:
                fp.write(json.dumps(x) + "\n")

# Argumentos de setup
model = sys.argv[1]  # Nome do LLM
label = sys.argv[2]  # Label do prompt
output_got_file = sys.argv[3]  # Ficheiro c/ output gerado pelo LLM em formato string
language = sys.argv[4] # Linguagem do benchmark

with open(output_got_file, 'r') as prompt_file:
    output_got = prompt_file.read()

num_samples_per_task = 1  # Numero de execuções por prompts

samples = [
    dict(
        task_id=label.replace("_", "/"),
        generation=output_got
    ) for _ in range(num_samples_per_task)
]

# Caminho para o diretório de dados
data_directory = os.path.join(os.path.dirname(__file__), f"codegeex/benchmark/humaneval-x/{language}/data/")
os.makedirs(data_directory, exist_ok=True)

# Escrita das samples num ficheiro jsonl
write_jsonl(os.path.join(data_directory, f"samples_{model}_humaneval_{language}.jsonl"), samples, append=True)
