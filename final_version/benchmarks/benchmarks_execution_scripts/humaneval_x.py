import os, re

def run_human_eval_benchmark(model, language):
    """Calcula o score do benchmark HumanEval-x - neste momento apenas calcula o pass@1 mas mais tarde vou incluir o pass@10 e pass@100"""
    return_value = None

    # Calcula o(s) score(s) do benchmark HumanEval e coloca o resultado num ficheiro de texto    
    os.system(
        f"docker run -v $(pwd)/benchmarks/CodeGeeX:/workspace/CodeGeeX/ -it humaneval_x "
        f"bash /workspace/CodeGeeX/scripts/evaluate_humaneval_x.sh /workspace/CodeGeeX/generated_samples/samples_{model}_humaneval_{language}.jsonl {language} > human_eval_score.txt"
    )

    # Caso exista o ficheiro, iremos fazer parsing de "Total" e de "Correct", fazendo a divisão entre "Correct" e "Total"
    if os.path.exists(f"human_eval_score.txt"):
        os.system(f"cat human_eval_score.txt")
        with open(f"human_eval_score.txt", 'r') as file:
            # Lê o conteúdo do ficheiro
            content = file.read()

            # Usamos regex para o parsing
            match = re.search(r"Total:\s+(\d+)\s+Correct:\s+(\d+)", content)
            if match:
                total = int(match.group(1))
                correct = int(match.group(2))
                # Calculamos a proporção correct/total
                if total != 0:  # Avoid division by zero
                    return_value = correct / total
                else:
                    return_value = -1  # Default to -1 if total is 0

    else:
        print(f"Error: The file 'human_eval_score.txt' was not found.")

    # Apagamos o ficheiro de texto temporário
    os.system(f"rm human_eval_score.txt")

    # Aqui devolve os scores calculados no parsing (NOTE: no futuro isto irá ser um tuplo do tipo (pass@1, pass@10, pass@100))
    return return_value
