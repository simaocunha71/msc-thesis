# Lista de palavras para substituir "codegeex"
substituicoes = ["codellama", "deepseek", "llama3", "starling", "mistral", "zephyr"]

# Lista de nomes de arquivos originais
arquivos_originais = [
    "codegeex_cyberseceval_autocomplete_0shot.sh",
    "codegeex_cyberseceval_autocomplete_3shot.sh",
    "codegeex_cyberseceval_canary_exploit_0shot.sh",
    "codegeex_cyberseceval_canary_exploit_3shot.sh",
    "codegeex_cyberseceval_frr.sh",
    "codegeex_cyberseceval_instruct_0shot.sh",
    "codegeex_cyberseceval_instruct_3shot.sh",
    "codegeex_cyberseceval_interpreter.sh",
    "codegeex_cyberseceval_mitre.sh",
    "codegeex_humanevalx_cpp_0shot.sh",
    "codegeex_humanevalx_cpp_3shot.sh",
    "codegeex_humanevalx_go_0shot.sh",
    "codegeex_humanevalx_go_3shot.sh",
    "codegeex_humanevalx_java_0shot.sh",
    "codegeex_humanevalx_java_3shot.sh",
    "codegeex_humanevalx_js_0shot.sh",
    "codegeex_humanevalx_js_3shot.sh",
    "codegeex_humanevalx_python_0shot.sh",
    "codegeex_humanevalx_python_3shot.sh",
    "codegeex_mbpp_0shot.sh",
    "codegeex_mbpp_3shot.sh"
]

# Criação dos novos arquivos com as substituições
for palavra in substituicoes:
    for arquivo in arquivos_originais:
        # Substitui "codegeex" pela palavra da vez
        novo_arquivo = arquivo.replace("codegeex", palavra)
        
        # Cria o arquivo .sh vazio
        with open(novo_arquivo, 'w') as f:
            pass  # Não escreve nada, apenas cria o arquivo

print("Arquivos .sh gerados com sucesso!")
