import os
import re
import json, sys
from pathlib import Path
from utils import delete_files_with_keyword

# Global variable to indicate if running in a cluster
running_in_cluster = False

docker_container = "registry.cn-hangzhou.aliyuncs.com/codefuse/codefuseeval:latest"
singularity_container = "../container_v2/folder/teste.sif"

# Define command templates for Docker and Singularity
COMMAND_TEMPLATES = {
    "docker": {
        "unsanitized": {
            "codebleu": (
                "docker run "
                "-v $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
                f"-it {docker_container} "
                "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
                "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_mbpp.jsonl "
                "codebleu "
                "mbpp "
                "{pass_k}"

            ),
            "google_bleu": (
                "docker run "
                "-v $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
                f"-it {docker_container} "
                "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
                "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_mbpp.jsonl "
                "google_bleu "
                "mbpp "
                "{pass_k}"

            ),
            "sacrebleu": (
                "python3 benchmarks/codefuse-evaluation/codefuseEval/evaluation.py "
                "--input_file benchmarks/codefuse-evaluation/codefuseEval/result/samples_{model}_mbpp.jsonl "
                "--metric sacrebleu "
                "--problem_file mbpp "
                "--k_max_value {pass_k} "
                "--test_groundtruth False"
            )
        },
        "sanitized": {
            "codebleu": (
                "docker run "
                "-v $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
                f"-it {docker_container} "
                "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
                "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_mbpp-sanitized.jsonl "
                "codebleu "
                "mbpp "
                "{pass_k}"

            ),
            "google_bleu": (
                "docker run "
                "-v $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
                f"-it {docker_container} "
                "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
                "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_mbpp-sanitized.jsonl "
                "google_bleu "
                "mbpp "
                "{pass_k}"

            ),
            "sacrebleu": (
                "python3 benchmarks/codefuse-evaluation/codefuseEval/evaluation.py "
                "--input_file benchmarks/codefuse-evaluation/codefuseEval/result/samples_{model}_mbpp-sanitized.jsonl "
                "--metric sacrebleu "
                "--problem_file mbpp "
                "--k_max_value {pass_k} "
                "--test_groundtruth False"
            )
        }
    },
    "singularity": {
        "unsanitized": {
            "codebleu": (
                "singularity exec "
                "--bind $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
                f"{singularity_container} "
                "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
                "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_mbpp.jsonl "
                "codebleu "
                "mbpp "
                "{pass_k}"

            ),
            "google_bleu": (
                "singularity exec "
                "--bind $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
                f"{singularity_container} "
                "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
                "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_mbpp.jsonl "
                "google_bleu "
                "mbpp "
                "{pass_k}"

            ),
            "sacrebleu": (
                "python3 benchmarks/codefuse-evaluation/codefuseEval/evaluation.py "
                "--input_file benchmarks/codefuse-evaluation/codefuseEval/result/samples_{model}_mbpp.jsonl "
                "--metric sacrebleu "
                "--problem_file mbpp "
                "--k_max_value {pass_k} "
                "--test_groundtruth False"
            )
        },
        "sanitized": {
            "codebleu": (
                "singularity exec "
                "--bind $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
                f"{singularity_container} "
                "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
                "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_mbpp-sanitized.jsonl "
                "codebleu "
                "mbpp "
                "{pass_k}"

            ),
            "google_bleu": (
                "singularity exec "
                "--bind $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
                f"{singularity_container} "
                "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
                "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_mbpp-sanitized.jsonl "
                "google_bleu "
                "mbpp "
                "{pass_k}"

            ),
            "sacrebleu": (
                "python3 benchmarks/codefuse-evaluation/codefuseEval/evaluation.py "
                "--input_file benchmarks/codefuse-evaluation/codefuseEval/result/samples_{model}_mbpp-sanitized.jsonl "
                "--metric sacrebleu "
                "--problem_file mbpp "
                "--k_max_value {pass_k} "
                "--test_groundtruth False"
            )
        }
    }
}

def execute_command(command: str):
    """Executes a system command."""
    os.system(command)

def extract_scores_from_json(file_googlebleu: Path, file_codebleu: Path, file_sacrebleu: Path) -> tuple:
    """Extracts google_bleu, codebleu, and sacrebleu scores from JSON files."""
    gbleu_score = -1
    codeb_score = -1
    sacreb_score = -1
    
    # Check and extract from google_bleu file
    if file_googlebleu.exists():
        with file_googlebleu.open('r') as file:
            for line in file:
                try:
                    data = json.loads(line)
                    if 'google_bleu' in data:
                        gbleu_score = data['google_bleu']
                except json.JSONDecodeError:
                    print(f"Error: Failed to decode JSON in '{file_googlebleu}'")
    else:
        print(f"Error: The file '{file_googlebleu}' was not found.")

    # Check and extract from codebleu file
    if file_codebleu.exists():
        with file_codebleu.open('r') as file:
            for line in file:
                try:
                    data = json.loads(line)
                    if 'CodeBLEU_Score' in data:
                        codeb_score = data['CodeBLEU_Score']
                except json.JSONDecodeError:
                    print(f"Error: Failed to decode JSON in '{file_codebleu}'")
    else:
        print(f"Error: The file '{file_codebleu}' was not found.")

    # Check and extract from sacrebleu file
    if file_sacrebleu.exists():
        with file_sacrebleu.open('r') as file:
            for line in file:
                try:
                    data = json.loads(line)
                    if 'score' in data:
                        sacreb_score = data['score']
                except json.JSONDecodeError:
                    print(f"Error: Failed to decode JSON in '{file_sacrebleu}'")
    else:
        print(f"Error: The file '{file_sacrebleu}' was not found.")

    return gbleu_score, codeb_score, sacreb_score


def parse_scores(file_path):
    """Parse the pass@1, pass@10, and pass@100 scores from a given file."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            match_pass1 = re.findall(r"pass@1:\s+([-+]?\d*\.\d+|\d+)", content)
            match_pass10 = re.findall(r"pass@10:\s+([-+]?\d*\.\d+|\d+)", content)
            match_pass100 = re.findall(r"pass@100:\s+([-+]?\d*\.\d+|\d+)", content)
            
            # Exibe todos os matches encontrados
            print("pass@1 matches:", match_pass1)
            print("pass@10 matches:", match_pass10)
            print("pass@100 matches:", match_pass100)
            
            # Inicializa a lista de resultados
            results = []
            
            # Adiciona os valores encontrados às respostas, se existirem
            results.extend(match_pass1[:2])   # Adiciona até 2 valores de pass@1
            results.extend(match_pass10[:2])  # Adiciona até 2 valores de pass@10
            results.extend(match_pass100[:2]) # Adiciona até 2 valores de pass@100
            
            # Preenche com -1 se a lista tiver menos de 6 elementos
            while len(results) < 6:
                results.append(-1)
            
            return tuple(results)  # Retorna os resultados como tupla
            
    else:
        print(f"Error: The file '{file_path}' was not found.")
        return None

def run_mbpp_benchmark(model: str, pass_k : int) -> tuple:
    """Calculates the MBPP+ benchmark scores."""

    base_path = Path("benchmarks/codefuse-evaluation/codefuseEval/result")
    base_path.mkdir(parents=True, exist_ok=True)
    
    execute_command(f"python3 benchmarks/evalplus/evalplus/evaluate_mbpp.py --dataset mbpp --k_max_value {pass_k} --samples benchmarks/evalplus/results/samples_{model}_mbpp.jsonl > mbpp_score.txt")
    os.system(f"cp benchmarks/evalplus/results/samples_{model}_mbpp.jsonl benchmarks/codefuse-evaluation/codefuseEval/result")


    scores = {"MBPP (unsanitized) pass@1": -1, "MBPP+ (unsanitized) pass@1": -1, 
              "MBPP (unsanitized) pass@10": -1, "MBPP+ (unsanitized) pass@10": -1, 
              "MBPP (unsanitized) pass@100": -1, "MBPP+ (unsanitized) pass@100": -1, 
              "GoogleBLEU (unsanitized)": -1, "CodeBLEU (unsanitized)": -1, "SacreBLEU (unsanitized)": -1,
              
              "MBPP (sanitized) pass@1": -1, "MBPP+ (sanitized) pass@1": -1, 
              "MBPP (sanitized) pass@10": -1, "MBPP+ (sanitized) pass@10": -1, 
              "MBPP (sanitized) pass@100": -1, "MBPP+ (sanitized) pass@100": -1, 
              "GoogleBLEU (sanitized)": -1, "CodeBLEU (sanitized)": -1, "SacreBLEU (sanitized)": -1}

    command_set = COMMAND_TEMPLATES["singularity" if running_in_cluster else "docker"]

    for key in ["unsanitized"]:
        for metric, command_template in command_set[key].items():
            command = command_template.format(model=model, pass_k=pass_k)
            execute_command(command)

    # Update scores for Google BLEU, CodeBLEU, and SacreBLEU for unsanitized
    unsanitized_google_bleu_path = base_path / f"samples_{model}_mbpp_google_bleu.jsonl"
    unsanitized_codebleu_path = base_path / f"samples_{model}_mbpp_codebleu.jsonl"
    unsanitized_sacrebleu_path = base_path / f"samples_{model}_mbpp_sacrebleu.jsonl"

    scores["MBPP (unsanitized) pass@1"], scores["MBPP+ (unsanitized) pass@1"], scores["MBPP (unsanitized) pass@10"], scores["MBPP+ (unsanitized) pass@10"], scores["MBPP (unsanitized) pass@100"], scores["MBPP+ (unsanitized) pass@100"] = parse_scores("mbpp_score.txt")
    scores["GoogleBLEU (unsanitized)"], scores["CodeBLEU (unsanitized)"], scores["SacreBLEU (unsanitized)"] = extract_scores_from_json(unsanitized_google_bleu_path, unsanitized_codebleu_path, unsanitized_sacrebleu_path)


    # Execute the remaining scripts
    execute_command(f"python3 benchmarks/evalplus/evalplus/sanitize.py --samples benchmarks/evalplus/results/samples_{model}_mbpp.jsonl")
    execute_command(f"python3 benchmarks/evalplus/evalplus/syncheck.py --samples benchmarks/evalplus/results/samples_{model}_mbpp-sanitized.jsonl --dataset mbpp")
    execute_command(f"python3 benchmarks/evalplus/evalplus/evaluate_mbpp.py --dataset mbpp --k_max_value {pass_k} --samples benchmarks/evalplus/results/samples_{model}_mbpp-sanitized.jsonl > mbpp_score_sanitized.txt")

    os.system(f"cp benchmarks/evalplus/results/samples_{model}_mbpp-sanitized.jsonl benchmarks/codefuse-evaluation/codefuseEval/result")
    sanitized_google_bleu_path = base_path / f"samples_{model}_mbpp-sanitized_google_bleu.jsonl"
    sanitized_codebleu_path = base_path / f"samples_{model}_mbpp-sanitized_codebleu.jsonl"
    sanitized_sacrebleu_path = base_path / f"samples_{model}_mbpp-sanitized_sacrebleu.jsonl"

    for key in ["sanitized"]:
        for metric, command_template in command_set[key].items():
            command = command_template.format(model=model, pass_k=pass_k)
            execute_command(command)

    scores["MBPP (sanitized) pass@1"], scores["MBPP+ (sanitized) pass@1"], scores["MBPP (sanitized) pass@10"], scores["MBPP+ (sanitized) pass@10"], scores["MBPP (sanitized) pass@100"], scores["MBPP+ (sanitized) pass@100"] = parse_scores("mbpp_score_sanitized.txt")
    scores["GoogleBLEU (sanitized)"], scores["CodeBLEU (sanitized)"], scores["SacreBLEU (sanitized)"] = extract_scores_from_json(sanitized_google_bleu_path, sanitized_codebleu_path, sanitized_sacrebleu_path)

    execute_command("rm mbpp_score.txt")
    execute_command("rm mbpp_score_sanitized.txt")
    
    delete_files_with_keyword("benchmarks/codefuse-evaluation/codefuseEval/result", "mbpp")

    return (
        scores["MBPP (unsanitized) pass@1"], scores["MBPP (sanitized) pass@1"],
        scores["MBPP+ (unsanitized) pass@1"], scores["MBPP+ (sanitized) pass@1"],

        scores["MBPP (unsanitized) pass@10"], scores["MBPP (sanitized) pass@10"],
        scores["MBPP+ (unsanitized) pass@10"], scores["MBPP+ (sanitized) pass@10"],

        scores["MBPP (unsanitized) pass@100"], scores["MBPP (sanitized) pass@100"],
        scores["MBPP+ (unsanitized) pass@100"], scores["MBPP+ (sanitized) pass@100"],

        scores["GoogleBLEU (unsanitized)"], scores["GoogleBLEU (sanitized)"],
        scores["CodeBLEU (unsanitized)"], scores["CodeBLEU (sanitized)"],
        scores["SacreBLEU (unsanitized)"], scores["SacreBLEU (sanitized)"]
    )