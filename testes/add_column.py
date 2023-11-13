import csv

def preencher_coluna_com_valor(input_file, output_file, nome_coluna, valor_preencher):
    # Lê o arquivo CSV de entrada
    with open(input_file, 'r') as csv_in:
        reader = csv.DictReader(csv_in)
        header = reader.fieldnames

        # Verifica se a coluna especificada existe no cabeçalho
        if nome_coluna not in header:
            raise ValueError(f"A coluna '{nome_coluna}' não existe no arquivo CSV.")

        # Lê todas as linhas e preenche os valores na coluna específica com o valor fornecido
        rows = list(reader)
        for row in rows:
            if nome_coluna not in row or not row[nome_coluna]:
                row[nome_coluna] = valor_preencher

    # Escreve o arquivo CSV de saída
    with open(output_file, 'w', newline='') as csv_out:
        writer = csv.DictWriter(csv_out, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)

# Exemplo de uso com um único valor
valor_para_adicionar = 'ValorADD'

preencher_coluna_com_valor('input.csv', 'output.csv', nome_coluna='ColunaNova', valor_preencher=valor_para_adicionar)
