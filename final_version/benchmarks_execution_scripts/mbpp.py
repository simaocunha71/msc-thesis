import os
import re

def run_mbpp_benchmark(model):
    """Calculates the score of the MBPP benchmark - currently only calculates pass@1 but will include pass@10 and pass@100 later."""
    return_value = None

    # Calculate the benchmark score and place the result in a text file
    os.system("export PYTHONPATH=$PYTHONPATH:$(pwd)")
    os.system(f"python3 evalplus/evalplus/evaluate.py --dataset mbpp --samples evalplus/results/samples_{model}_mbpp.jsonl > mbpp_score.txt")


    # If the file exists, we will parse pass@1, pass@10, and pass@100
    if os.path.exists("mbpp_score.txt"):
        with open("mbpp_score.txt", 'r') as file:
            # Read the content of the file at once
            content = file.read()
            # Use regex for parsing
            match = re.search(r"mbpp\+\s*\(base\s*\+\s*extra\s*tests\)\npass@1:\s+([-+]?\d*\.\d+|\d+)", content)
            if match:
                # Extract the value of pass@1
                return_value = match.group(1)
            else:
                print("Error: Pattern not found in file.")
    else:
        print("Error: The file 'mbpp_score.txt' was not found.")

    # Delete the temporary text file
    os.system("rm mbpp_score.txt")

    # Return the calculated scores from parsing (NOTE: in the future, this will be a tuple of the form (pass@1, pass@10, pass@100))

    return return_value
