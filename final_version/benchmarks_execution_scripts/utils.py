import csv
import pandas as pd
import json

def autocompleteOrInstruct_json_to_csv(json_responses, json_results, csv_file_path, columns):
    """Pega nas colunas da lista 'columns' de um ficheiro JSON de respostas do benchmark Autocomplete ou Instruct
    e adiciona ao ficheiro CSV que irá ter todos os resultados deste benchmark"""

    """
    TODO: pegar no json_results e replicar cada uma das linhas do dataframe df quantas entradas existirem no json
    Em cada linha do df, deve conter language, bleu, total_count, vulnerable_percentage, vulnerable_suggestion_count, pass_rate
    """

    # Read JSON data from the file
    with open(json_responses, 'r') as file:
        json_response_data = json.load(file)

    # Convert JSON to DataFrame
    df = pd.DataFrame(json_response_data)

    # Select only specified columns
    df = df[columns]

    # Define custom column "Benchmark prompt" by concatenating "variant", "_" and "prompt_id"
    df['Benchmark prompt'] = df['variant'] + '_' + df['prompt_id'].astype(str)
    df = df.drop(['variant', 'prompt_id'], axis=1)

    # Move 'Benchmark prompt' column to the second position
    cols = list(df.columns)
    cols.insert(1, cols.pop(cols.index('Benchmark prompt')))
    df = df[cols]

    # Append DataFrame to existing CSV file
    df.to_csv(csv_file_path, mode='a', index=False, header=False)

def add_score_in_csv(csv_file_old, csv_file_new, column_name, value_to_add):
    """Adiciona um valor numa coluna de um ficheiro CSV já existente"""
    
    # Lê o ficheiro CSV de entrada (s/ o HumanEvalScore)
    with open(csv_file_old, 'r') as csv_in:
        reader = csv.DictReader(csv_in)
        header = reader.fieldnames

        # Verifica se a coluna à qual queremos adicionar o score existe no ficheiro CSV de input
        if column_name not in header:
            raise ValueError(f"A coluna '{column_name}' não existe no ficheiro CSV de input.")

        # Lê todas as linhas e preenche os valores na coluna específica com o valor dado do score
        rows = list(reader)
        for row in rows:
            if column_name not in row or not row[column_name]:
                row[column_name] = value_to_add

    # Escreve o ficheiro CSV de output
    with open(csv_file_new, 'w', newline='') as csv_out:
        writer = csv.DictWriter(csv_out, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)