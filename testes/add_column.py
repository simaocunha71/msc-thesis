import csv

def preencher_coluna_com_lista(input_file, output_file, nome_coluna, valores_preencher):
    # Lê o arquivo CSV de entrada
    with open(input_file, 'r') as csv_in:
        reader = csv.DictReader(csv_in)
        header = reader.fieldnames

        # Verifica se a coluna especificada existe no cabeçalho
        if nome_coluna not in header:
            raise ValueError(f"A coluna '{nome_coluna}' não existe no arquivo CSV.")

        # Lê todas as linhas e preenche os valores na coluna específica com a lista fornecida
        rows = list(reader)
        for i, row in enumerate(rows):
            if nome_coluna not in row or not row[nome_coluna]:
                try:
                    valor_preencher = valores_preencher[i]
                except IndexError:
                    raise ValueError("Número insuficiente de valores na lista para preencher a coluna.")

                row[nome_coluna] = valor_preencher

    # Escreve o arquivo CSV de saída
    with open(output_file, 'w', newline='') as csv_out:
        writer = csv.DictWriter(csv_out, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)

# Exemplo de uso com uma lista de valores
valores_para_adicionar = ['Valor1', 'Valor2', 'Valor3', 'Valor4']

preencher_coluna_com_lista('input.csv', 'output.csv', nome_coluna='ColunaNova', valores_preencher=valores_para_adicionar)
