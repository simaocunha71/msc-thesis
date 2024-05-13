import gzip
import json
import os
from typing import Iterable, Dict
import sys

def write_jsonl(filename: str, data: Iterable[Dict], append: bool = False):
    """
    Writes an iterable of dictionaries to jsonl
    """
    if append:
        mode = 'ab'
    else:
        mode = 'wb'
    filename = os.path.expanduser(filename)
    if filename.endswith(".gz"):
        with open(filename, mode) as fp:
            with gzip.GzipFile(fileobj=fp, mode='wb') as gzfp:
                for x in data:
                    gzfp.write((json.dumps(x) + "\n").encode('utf-8'))
    else:
        with open(filename, mode) as fp:
            for x in data:
                fp.write((json.dumps(x) + "\n").encode('utf-8'))

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

outputs_directory = "benchmarks/CodeGeeX/generated_samples"
if not os.path.exists(outputs_directory):
    os.makedirs(outputs_directory)

# Escrita das samples num ficheiro jsonl
write_jsonl(f"{outputs_directory}/samples_{model}_humaneval_{language}.jsonl", samples, append=True)
