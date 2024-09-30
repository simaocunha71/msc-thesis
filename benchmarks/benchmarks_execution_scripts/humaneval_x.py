import os, re, json, sys
from pathlib import Path
from benchmarks.benchmarks_execution_scripts.utils import delete_files_with_keyword

# Global variable to indicate if running in a cluster
running_in_cluster = False

docker_container = "registry.cn-hangzhou.aliyuncs.com/codefuse/codefuseeval:latest"
singularity_container = "../container_in_use/codefuseeval_latest.sif"

# Define command templates for Docker and Singularity
COMMAND_TEMPLATES = {
    "docker": {
        "pass@k": (
            "docker run "
            "-v $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
            f"-it {docker_container} "
            "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
            "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}_{n_shot}_shot.jsonl "
            "pass@k "
            "humaneval_{language} {pass_k} > human_eval_score.txt"
        ),
        "codebleu": (
            "docker run "
            "-v $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
            f"-it {docker_container} "
            "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
            "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}_{n_shot}_shot.jsonl "
            "codebleu "
            "humaneval_{language} "
            "{pass_k}"
        ),
        "google_bleu": (
            "docker run "
            "-v $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
            f"-it {docker_container} "
            "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
            "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}_{n_shot}_shot.jsonl "
            "google_bleu "
            "humaneval_{language} "
            "{pass_k}"
        ),
        "sacrebleu": (
            "python3 benchmarks/codefuse-evaluation/codefuseEval/evaluation.py "
            "--input_file benchmarks/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}_{n_shot}_shot.jsonl "
            "--metric sacrebleu "
            "--problem_file humaneval_{language} "
            "--k_max_value {pass_k} "
            "--test_groundtruth False"
        )
    },
    "singularity": {
        "pass@k": (
            "singularity exec "
            "--bind $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
            f"{singularity_container} "
            "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
            "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}_{n_shot}_shot.jsonl "
            "pass@k "
            "humaneval_{language} {pass_k} > human_eval_score.txt"
        ),
        "codebleu": (
            "singularity exec "
            "--bind $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
            f"{singularity_container} "
            "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
            "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}_{n_shot}_shot.jsonl "
            "codebleu "
            "humaneval_{language} "
            "{pass_k}"
        ),
        "google_bleu": (
            "singularity exec "
            "--bind $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
            f"{singularity_container} "
            "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
            "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}_{n_shot}_shot.jsonl "
            "google_bleu "
            "humaneval_{language} "
            "{pass_k}"
        ),
        "sacrebleu": (
            "python3 benchmarks/codefuse-evaluation/codefuseEval/evaluation.py "
            "--input_file benchmarks/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}_{n_shot}_shot.jsonl "
            "--metric sacrebleu "
            "--problem_file humaneval_{language} "
            "--k_max_value {pass_k}"
            "--test_groundtruth False"
        )
    }
}

def execute_command(command: str) -> None:
    """
    Executes a system command.
    Args:
        command (str): The command to be executed in the system shell.
    """
    os.system(command)

def parse_score_from_file(file_path: Path) -> dict:
    """
    Parse the pass@1, pass@10, and pass@100 scores from a given file.
    Args:
        file_path (Path): Text file containing all the pass@k scores.
    Returns:
        dict: contains all the pass@k scores
    """
    scores = {"pass_1": -1, "pass_10": -1, "pass_100": -1}
    
    if file_path.exists():
        with file_path.open('r') as file:
            content = file.read()

            match_pass1 = re.search(r"'pass@1': (\d+\.\d+)", content)
            match_pass10 = re.search(r"'pass@10': (\d+\.\d+)", content)
            match_pass100 = re.search(r"'pass@100': (\d+\.\d+)", content)

            if match_pass1:
                scores["pass_1"] = match_pass1.group(1)
            if match_pass10:
                scores["pass_10"] = match_pass10.group(1)
            if match_pass100:
                scores["pass_100"] = match_pass100.group(1)

    else:
        print(f"Error: The file '{file_path}' was not found.")
    
    return scores

def extract_scores_from_json(file_googlebleu: Path, file_codebleu: Path, file_sacrebleu: Path) -> dict:
    """
    Extracts the google_bleu, codebleu, and sacrebleu scores from the JSON files.
    Args:
        file_googlebleu (Path): File containg the GoogleBLEU
        file_codebleu (Path): File containg the CodeBLEU
        file_sacrebleu (Path): File containg the SacreBLEU
    Returns:
        dict: contains all the BLEU's scores
    """
    scores = {"google_bleu": -1, "codebleu": -1, "sacrebleu": -1}
    
    # Check and extract from google_bleu file
    if file_googlebleu.exists():
        with file_googlebleu.open('r') as file:
            for line in file:
                try:
                    data = json.loads(line)
                    if 'google_bleu' in data:
                        scores["google_bleu"] = data['google_bleu']
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
                        scores["codebleu"] = data['CodeBLEU_Score']
                except json.JSONDecodeError:
                    print(f"Error: Failed to decode JSON in '{file_codebleu}'")

    # Check and extract from codebleu file
    if file_sacrebleu.exists():
        with file_sacrebleu.open('r') as file:
            for line in file:
                try:
                    data = json.loads(line)
                    if 'score' in data:
                        scores["sacrebleu"] = data['score']
                except json.JSONDecodeError:
                    print(f"Error: Failed to decode JSON in '{file_sacrebleu}'")
    else:
        print(f"Error: The file '{file_sacrebleu}' was not found.")
    
    return scores


def run_human_eval_benchmark(model: str, language: str, pass_k: int, n_shot: str) -> dict:
    """
    Calculates the HumanEval-X benchmark scores.
    Args:
        model (str): LLM path.
        language (str): Language of the HumanEval-X benchmark.
        pass_k (int): Max k value for pass@k (k = 1, 10, 100).
        n_shot (int): Number of shots (examples) for each execution.
    Returns:
        dict: All the pass@k, CodeBLEU, SacreBLEU and GoogleBLEU for a given language of HumanEval-X
    """
    base_path = Path("benchmarks/codefuse-evaluation/codefuseEval/result")
    scores = {"pass_1": -1, "pass_10": -1, "pass_100": -1,
              "google_bleu": -1, "codebleu": -1, "sacrebleu": -1}

    # Determine the appropriate command template
    if running_in_cluster:
        command_templates = COMMAND_TEMPLATES["singularity"]
    else:
        command_templates = COMMAND_TEMPLATES["docker"]

    # Execute commands for each metric
    for metric, command_template in command_templates.items():
        command = command_template.format(model=model, language=language, pass_k=pass_k, n_shot=n_shot)
        execute_command(command)
    
    # Update scores for pass@k
    scores.update(parse_score_from_file(Path("human_eval_score.txt")))

    # Extract scores for Google BLEU, CodeBLEU, and SacreBLEU
    google_bleu_path = base_path / f"samples_{model}_humaneval_{language}_{n_shot}_shot_google_bleu.jsonl"
    codebleu_path = base_path / f"samples_{model}_humaneval_{language}_{n_shot}_shot_codebleu.jsonl"
    sacrebleu_path = base_path / f"samples_{model}_humaneval_{language}_{n_shot}_shot_sacrebleu.jsonl"
    scores.update(extract_scores_from_json(google_bleu_path, codebleu_path, sacrebleu_path))
    
    # Cleanup
    os.system("rm human_eval_score.txt")
    delete_files_with_keyword("benchmarks/codefuse-evaluation/codefuseEval/result", "codebleu")
    delete_files_with_keyword("benchmarks/codefuse-evaluation/codefuseEval/result", "sacrebleu")
    delete_files_with_keyword("benchmarks/codefuse-evaluation/codefuseEval/result", "google_bleu")

    return scores
