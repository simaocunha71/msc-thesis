import os, re

def run_mbpp_benchmark(model):
    """Calculates the score of the MBPP benchmark - currently only calculates pass@1 but will include pass@10 and pass@100 later."""
    pass_1_mbpp = pass_1_mbppPlus = pass_1_mbpp_sanitized = pass_1_mbppPlus_sanitized = None

    def run_command(command):
        """Run a shell command and check for errors."""
        result = os.system(command)
        if result != 0:
            print(f"Error running command: {command}")
    
    def parse_scores(file_path):
        """Parse the pass@1 and pass@1Plus scores from a given file."""
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                matches = re.findall(r"pass@1:\s+([-+]?\d*\.\d+|\d+)", content)
                if matches and len(matches) >= 2:
                    return matches[:2]
                else:
                    print(f"Error: Pattern not found in file {file_path}.")
        else:
            print(f"Error: The file '{file_path}' was not found.")
        return None, None

    #os.system("export PYTHONPATH=$PYTHONPATH:$(pwd)")
    os.environ["PYTHONPATH"] = os.environ.get("PYTHONPATH", "") + ":$(pwd)"

    run_command(f"python3 benchmarks/evalplus/evalplus/sanitize.py --samples benchmarks/evalplus/results/samples_{model}_mbpp.jsonl")
    run_command(f"python3 benchmarks/evalplus/evalplus/syncheck.py --samples benchmarks/evalplus/results/samples_{model}_mbpp-sanitized.jsonl --dataset mbpp")
    run_command(f"python3 benchmarks/evalplus/evalplus/evaluate.py --dataset mbpp --samples benchmarks/evalplus/results/samples_{model}_mbpp-sanitized.jsonl > mbpp_score_sanitized.txt")
    run_command(f"python3 benchmarks/evalplus/evalplus/evaluate.py --dataset mbpp --samples benchmarks/evalplus/results/samples_{model}_mbpp.jsonl > mbpp_score.txt")

    pass_1_mbpp_sanitized, pass_1_mbppPlus_sanitized = parse_scores("mbpp_score_sanitized.txt")
    pass_1_mbpp, pass_1_mbppPlus = parse_scores("mbpp_score.txt")

    run_command("rm mbpp_score.txt")
    run_command("rm mbpp_score_sanitized.txt")

    return pass_1_mbpp, pass_1_mbppPlus, pass_1_mbpp_sanitized, pass_1_mbppPlus_sanitized
