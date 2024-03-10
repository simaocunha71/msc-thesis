import os
import re

def run_instruct_benchmark(model, language):
    """Calcula os scores do benchmark Instruct do CybersecEval"""
    return_value = None

    # Calcula os scores do benchmark Instruct do CybersecEval e coloca os resultados num ficheiro de JSON 
    # TODO: Executar comando do repositorio Github deles (Dica: ver run_instruct.sh)
    os.system(
        "ls"
    )

    # TODO: Usar o ficheiro json dos resultados e guardar todas as variáveis num tuplo
    if os.path.exists(f"cyberseceval_instruct_results.txt"):
        os.system(f"cat cyberseceval_instruct_results.txt")
        with open(f"cyberseceval_instruct_results.txt", 'r') as file:
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
        print(f"Error: The file 'cyberseceval_instruct_results.txt' was not found.")

    # Apagamos o ficheiro de texto temporário
    os.system(f"rm cyberseceval_instruct_results.txt")

    # Aqui devolve os scores calculados no parsing (NOTE: no futuro isto irá ser um tuplo do tipo (pass@1, pass@10, pass@100))
    return return_value
