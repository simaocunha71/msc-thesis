import json
from pprint import pprint

def ler_json_contar_entradas_e_imprimir_entrada(file_path, posicao):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Verifica se o arquivo é uma lista
            if isinstance(data, list):
                num_entradas = len(data)
                print(f"O arquivo contém {num_entradas} entradas.")

                if posicao < num_entradas:
                    entrada = data[posicao]
                    print(f"A entrada na posição {posicao} é:")
                    pprint(entrada)
                else:
                    print(f"A posição {posicao} não existe no arquivo.")
            else:
                print("O arquivo JSON não contém uma lista.")
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")

# Exemplo de uso:
arquivo_json = "autocomplete.json"  # Substitua pelo caminho do seu arquivo JSON
posicao_desejada = 802  # Substitua pela posição desejada

ler_json_contar_entradas_e_imprimir_entrada(arquivo_json, posicao_desejada)
