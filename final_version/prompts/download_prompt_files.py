import os
import requests
import shutil
import gzip

def download_file(url, folder):
    print(f"Downloading {url}")
    # Cria a pasta se não existir
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Obtém o nome do arquivo a partir do URL
    filename = os.path.join(folder, url.split('/')[-1])

    # Faz o download do arquivo
    with requests.get(url) as response:
        with open(filename, 'wb') as file:
            file.write(response.content)

    # Se o arquivo for um .gz, descomprime
    if filename.endswith('.gz'):
        with gzip.open(filename, 'rb') as f_in:
            with open(filename[:-3], 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        # Remove o arquivo comprimido
        os.remove(filename)

print(f"Downloading HumanEval-X JSON files")
download_file("https://github.com/THUDM/CodeGeeX/raw/main/codegeex/benchmark/humaneval-x/cpp/data/humaneval_cpp.jsonl.gz", "humaneval_x")
download_file("https://github.com/THUDM/CodeGeeX/raw/main/codegeex/benchmark/humaneval-x/go/data/humaneval_go.jsonl.gz", "humaneval_x")
download_file("https://github.com/THUDM/CodeGeeX/raw/main/codegeex/benchmark/humaneval-x/java/data/humaneval_java.jsonl.gz", "humaneval_x")
download_file("https://github.com/THUDM/CodeGeeX/raw/main/codegeex/benchmark/humaneval-x/js/data/humaneval_js.jsonl.gz", "humaneval_x")
download_file("https://github.com/THUDM/CodeGeeX/raw/main/codegeex/benchmark/humaneval-x/python/data/humaneval_python.jsonl.gz", "humaneval_x")

print(f"Downloading MBPP JSON file")
download_file("https://github.com/evalplus/mbppplus_release/releases/download/v0.2.0/MbppPlus.jsonl.gz", "mbpp")

print(f"Downloading CyberSecEval JSON files")
download_file("https://raw.githubusercontent.com/meta-llama/PurpleLlama/main/CybersecurityBenchmarks/datasets/autocomplete/autocomplete.json", "cyberseceval")
download_file("https://raw.githubusercontent.com/meta-llama/PurpleLlama/main/CybersecurityBenchmarks/datasets/instruct/instruct.json", "cyberseceval")
download_file("https://raw.githubusercontent.com/meta-llama/PurpleLlama/main/CybersecurityBenchmarks/datasets/mitre/mitre_benchmark_100_per_category_with_augmentation.json", "cyberseceval")

