import os
import re
import json
from pathlib import Path

#sh benchmarks/codefuse-evaluation/codefuseEval/script/evaluation.sh benchmarks/codefuse-evaluation/codefuseEval/result/samples_llama-2-7b.Q2_K_humaneval_python.jsonl sacrebleu humaneval_python
# Global variable to indicate if running in a cluster
running_in_cluster = False

# Define command templates for Docker and Singularity
COMMAND_TEMPLATES = {
    "docker": {
        "pass@k": (
            "docker run "
            "-v $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
            "-it registry.cn-hangzhou.aliyuncs.com/codefuse/codefuseeval:latest "
            "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
            "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}.jsonl "
            "pass@k "
            "humaneval_{language} > human_eval_score.txt"
        ),
        "codebleu": (
            "docker run "
            "-v $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
            "-it registry.cn-hangzhou.aliyuncs.com/codefuse/codefuseeval:latest "
            "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
            "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}.jsonl "
            "codebleu "
            "humaneval_{language}"
        ),
        "google_bleu": (
            "docker run "
            "-v $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
            "-it registry.cn-hangzhou.aliyuncs.com/codefuse/codefuseeval:latest "
            "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
            "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}.jsonl "
            "google_bleu "
            "humaneval_{language}"
        ),
        "sacrebleu": (
            "python3 benchmarks/codefuse-evaluation/codefuseEval/evaluation.py "
            "--input_file benchmarks/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}.jsonl "
            "--metric sacrebleu "
            "--problem_file humaneval_{language} "
            "--test_groundtruth False"
        )
    },
    "singularity": {
        "pass@k": (
            "singularity exec "
            "--bind $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
            "../humaneval_x_dockerImage/humaneval_x.sif "
            "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
            "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}.jsonl "
            "pass@k "
            "humaneval_{language} > human_eval_score.txt"
        ),
        "codebleu": (
            "singularity exec "
            "--bind $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
            "../humaneval_x_dockerImage/humaneval_x.sif "
            "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
            "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}.jsonl "
            "codebleu "
            "humaneval_{language}"
        ),
        "google_bleu": (
            "singularity exec "
            "--bind $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
            "../humaneval_x_dockerImage/humaneval_x.sif "
            "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
            "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}.jsonl "
            "google_bleu "
            "humaneval_{language}"
        ),
        "sacrebleu": (
            "singularity exec "
            "--bind $(pwd)/benchmarks/codefuse-evaluation:/workspace/codefuse-evaluation/ "
            "../humaneval_x_dockerImage/humaneval_x.sif "
            "bash /workspace/codefuse-evaluation/codefuseEval/script/evaluation.sh "
            "/workspace/codefuse-evaluation/codefuseEval/result/samples_{model}_humaneval_{language}.jsonl "
            "sacrebleu "
            "humaneval_{language}"
        )
    }
}

def execute_command(command: str):
    """Executes a system command."""
    os.system(command)

def parse_score_from_file(file_path: Path) -> dict:
    """Parses score information from the given file."""
    scores = {"pass_1": -1, "google_bleu": -1, "codebleu": -1}
    
    if file_path.exists():
        with file_path.open('r') as file:
            content = file.read()
            match = re.search(r"Total:\s+(\d+)\s+Correct:\s+(\d+)", content)
            if match:
                total, correct = int(match.group(1)), int(match.group(2))
                if total != 0:
                    scores["pass_1"] = correct / total

    else:
        print(f"Error: The file '{file_path}' was not found.")
    
    return scores

def extract_scores_from_json(file_googlebleu: Path, file_codebleu: Path, file_sacrebleu: Path) -> dict:
    """Extracts google_bleu and codebleu scores from JSON files."""
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


def run_human_eval_benchmark(model: str, language: str) -> tuple:
    """Calculates the HumanEval-X benchmark scores."""
    base_path = Path("benchmarks/codefuse-evaluation/codefuseEval/result")
    scores = {"pass_1": -1, "google_bleu": -1, "codebleu": -1, "sacrebleu": -1}
    
    if running_in_cluster:
        command_templates = COMMAND_TEMPLATES["singularity"]
    else:
        command_templates = COMMAND_TEMPLATES["docker"]

    for metric, command_template in command_templates.items():
        command = command_template.format(model=model, language=language)
        execute_command(command)
        
    # Update scores for pass@k
    scores.update(parse_score_from_file(Path("human_eval_score.txt")))

    # Update scores for Google BLEU and CodeBLEU
    google_bleu_path = base_path / f"samples_{model}_humaneval_{language}_google_bleu.jsonl"
    codebleu_path = base_path / f"samples_{model}_humaneval_{language}_codebleu.jsonl"
    sacrebleu_path = base_path / f"samples_{model}_humaneval_{language}_sacrebleu.jsonl"
    scores.update(extract_scores_from_json(google_bleu_path, codebleu_path, sacrebleu_path))
    
    os.system("rm human_eval_score.txt")

    return (scores["pass_1"], scores["google_bleu"], scores["codebleu"], scores["sacrebleu"])
