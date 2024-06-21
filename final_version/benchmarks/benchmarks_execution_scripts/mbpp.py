import os
import re

using_sanitized_version = False

def run_mbpp_benchmark(model):
    """Calculates the score of the MBPP benchmark - currently only calculates pass@1 but will include pass@10 and pass@100 later."""
    pass_1_mbpp = pass_1_mbppPlus = None

    os.system("export PYTHONPATH=$PYTHONPATH:$(pwd)")
    if using_sanitized_version == True:
        # Calculate the benchmark score and place the result in a text file
        os.system(f"python3 benchmarks/evalplus/evalplus/sanitize.py --samples benchmarks/evalplus/results/samples_{model}_mbpp.jsonl")
        os.system(f"python3 benchmarks/evalplus/evalplus/syncheck.py --samples benchmarks/evalplus/results/samples_{model}_mbpp-sanitized.jsonl --dataset mbpp")
        os.system(f"python3 benchmarks/evalplus/evalplus/evaluate.py --dataset mbpp --samples benchmarks/evalplus/results/samples_{model}_mbpp-sanitized.jsonl > mbpp_score.txt")
    else:
        os.system(f"python3 benchmarks/evalplus/evalplus/evaluate.py --dataset mbpp --samples benchmarks/evalplus/results/samples_{model}_mbpp.jsonl > mbpp_score.txt")

    # If the file exists, we will parse pass@1 and pass@1Plus
    if os.path.exists("mbpp_score.txt"):
        with open("mbpp_score.txt", 'r') as file:
            # Read the content of the file at once
            content = file.read()
            # Use regex for parsing
            matches = re.findall(r"pass@1:\s+([-+]?\d*\.\d+|\d+)", content)

            if matches and len(matches) >= 2:
                # Extract the value of pass@1 and pass@1Plus
                pass_1_mbpp, pass_1_mbppPlus = matches[:2]
            else:
                print("Error: Pattern not found in file.")
    else:
        print("Error: The file 'mbpp_score.txt' was not found.")

    # Delete the temporary text file
    os.system("rm mbpp_score.txt")

    # Return the calculated scores from parsing
    return pass_1_mbpp, pass_1_mbppPlus
