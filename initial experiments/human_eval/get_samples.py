from data import write_jsonl, read_problems
import sys, subprocess, shlex

prompts_problems_file = sys.argv[1]

models = [
    "llama-2-7b.Q2_K"
]

def generate_one_completion(prompt, model):
    prompt = prompt.replace('"', r'\"').replace("'", r"\'").replace(">", r"\>").replace("<", r"\<").replace("\n", r'\n')

    # Use shlex.quote para escapar a string do prompt corretamente
    prompt = shlex.quote(prompt)

    command = f'python3 models/{model}.py {prompt} > {model}.output'
    subprocess.run(command, shell=True)

    with open(f"{model}.output", "r") as file:
        completion_output = file.read()
    
    subprocess.run("rm *.output", shell=True)
    return completion_output

for model in models:
    problems = read_problems()

    num_samples_per_task = 1
    samples = [
        dict(task_id=task_id, completion=generate_one_completion(problems[task_id]["prompt"], model))
        for task_id in problems
        for _ in range(num_samples_per_task)
    ]
    write_jsonl("samples_" + model + ".jsonl", samples)
