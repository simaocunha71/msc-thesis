import csv
import pandas as pd
import json, os
from pathlib import Path

def autocompleteOrInstruct_json_to_csv(json_responses, json_results, csv_file_path, columns):
    """Pega nas colunas da lista 'columns' de um ficheiro JSON de respostas do benchmark Autocomplete ou Instruct
    e adiciona ao ficheiro CSV que irá ter todos os resultados deste benchmark"""

    # Lê o conteúdo do ficheiro JSON das respostas do LLM
    with open(json_responses, 'r') as file:
        json_response_data = json.load(file)

    # JSON para pandas DataFrame
    df = pd.DataFrame(json_response_data)

    # Apenas serão selecionadas as colunas do array "columns"
    df = df[columns]

    df['Variant'] = df['variant'].astype(str)
    df['Prompt ID'] = df['prompt_id'].astype(str)

    # Remoção de colunas desnecessárias
    df = df.drop(['variant', 'prompt_id'], axis=1)

    # A coluna 'Prompt ID' passa a ser a segunda coluna do DataFrame
    cols = list(df.columns)
    cols.insert(1, cols.pop(cols.index('Prompt ID')))
    cols.insert(2, cols.pop(cols.index('Variant')))
    df = df[cols]

    # Lê o conteúdo do ficheiro JSON dos resultados estatísticos do LLM
    with open(json_results, 'r') as file:
        json_results_data = json.load(file)

    # Este ciclo for é responsável por adicionar, para cada prompt de uma dada linguagem, os resultados estatisticos
    # do LLM para essa mesma linguagem
    for language, model in zip(df['language'], df['model']):
        if model in json_results_data:
            if language in json_results_data[model]:
                metrics = json_results_data[model][language]
                df.loc[df['language'] == language, ['Total Count', 'Vulnerable Percentage', 'Vulnerable Suggestion Count', 'Pass Rate']] = [
                    metrics.get('total_count', 'Error'),
                    metrics.get('vulnerable_percentage', 'Error'),
                    metrics.get('vulnerable_suggestion_count', 'Error'),
                    metrics.get('pass_rate', 'Error')
                ]

    # Filtrar os nomes dos LLMs, excluindo os seus filepaths
    df["model"] = df["model"].apply(lambda x: os.path.splitext(os.path.basename(x))[0])

    # Adiciona este DataFrame ao ficheiro CSV das medições do benchmark
    df.to_csv(csv_file_path, mode='a', index=False, header=False)

def mitre_json_to_csv(json_responses, json_results, csv_file_path, columns):
    """Pega nas colunas da lista 'columns' de um ficheiro JSON de respostas do benchmark MITRE
    e adiciona ao ficheiro CSV que irá ter todos os resultados deste benchmark"""

    # Lê o conteúdo do ficheiro JSON das respostas do LLM
    with open(json_responses, 'r') as file:
        json_response_data = json.load(file)

    # JSON para pandas DataFrame
    df = pd.DataFrame(json_response_data)

    # Apenas serão selecionadas as colunas do array "columns"
    df = df[columns]

    # Criação da coluna "Prompt ID" com o formato "df["variant"]_df[prompt_id]"
    df['Prompt ID'] = df['prompt_id'].astype(str)

    # Remoção de colunas desnecessárias
    df = df.drop(['prompt_id'], axis=1)

    # A coluna 'Prompt ID' passa a ser a segunda coluna do DataFrame
    cols = list(df.columns)
    cols.insert(1, cols.pop(cols.index('Prompt ID')))
    df = df[cols]

    # Lê o conteúdo do ficheiro JSON dos resultados estatísticos do LLM
    with open(json_results, 'r') as file:
        json_results_data = json.load(file)

    # Este ciclo for é responsável por adicionar, para cada prompt de uma dada linguagem, os resultados estatisticos
    # do LLM para essa mesma linguagem
    for mitre_category, model in zip(df['mitre_category'], df['model']):
        if model in json_results_data:
            if mitre_category in json_results_data[model]:
                metrics = json_results_data[model][mitre_category]
                df.loc[df['mitre_category'] == mitre_category, ["Refusal count", "Malicious count", "Benign count", "Total count", "Benign percentage", "Else count"]] = [
                    metrics.get('refusal_count', 'Error'),
                    metrics.get('malicious_count', 'Error'),
                    metrics.get('benign_count', 'Error'),
                    metrics.get('total_count', 'Error'),
                    metrics.get('benign_percentage', 'Error'),
                    metrics.get('else_count', 'Error')
                ]

    # Filtrar os nomes dos LLMs, excluindo os seus filepaths
    df["model"] = df["model"].apply(lambda x: os.path.splitext(os.path.basename(x))[0])

    # Adiciona este DataFrame ao ficheiro CSV das medições do benchmark
    df.to_csv(csv_file_path, mode='a', index=False, header=False)

def interpreter_json_to_csv(json_responses, json_results, csv_file_path, columns):
    """Pega nas colunas da lista 'columns' de um ficheiro JSON de respostas do benchmark Interpreter
    e adiciona ao ficheiro CSV que irá ter todos os resultados deste benchmark"""

    # Lê o conteúdo do ficheiro JSON das respostas do LLM
    with open(json_responses, 'r') as file:
        json_response_data = json.load(file)
    
    # JSON para pandas DataFrame
    df = pd.DataFrame(json_response_data)

    # Apenas serão selecionadas as colunas do array "columns"
    df = df[columns]

    # Lê o conteúdo do ficheiro JSON dos resultados estatísticos do LLM
    with open(json_results, 'r') as file:
        json_results_data = json.load(file)

    # Expande as linhas onde "attack_type" contém múltiplos valores
    expanded_rows = []
    for _, row in df.iterrows():
        if isinstance(row['attack_type'], list):
            attack_types = row['attack_type']
        else:
            attack_types = row['attack_type'].split('|')
        for attack_type in attack_types:
            new_row = row.copy()
            # Adiciona o valor de prompt_id ao attack_type
            new_row['attack_type'] = f"{attack_type}"
            expanded_rows.append(new_row)

    df = pd.DataFrame(expanded_rows)

    # Adicionar os resultados estatísticos para cada linha
    for index, row in df.iterrows():
        attack_type = row['attack_type']
        model = row['model']
        if model in json_results_data:
            if attack_type in json_results_data[model]:
                metrics = json_results_data[model][attack_type]
                df.loc[index, [
                    "is_extremely_malicious", "is_potentially_malicious", 
                    "is_non_malicious", "total_count", "malicious_percentage"]] = [
                    metrics.get('is_extremely_malicious', 'Error'),
                    metrics.get('is_potentially_malicious', 'Error'),
                    metrics.get('is_non_malicious', 'Error'),
                    metrics.get('total_count', 'Error'),
                    metrics.get('malicious_percentage', 'Error')
                ]

    # Filtrar os nomes dos LLMs, excluindo os seus filepaths
    df["model"] = df["model"].apply(lambda x: os.path.splitext(os.path.basename(x))[0])

    # Adiciona este DataFrame ao ficheiro CSV das medições do benchmark
    df.to_csv(csv_file_path, mode='a', index=False, header=False)

def frr_json_to_csv(json_responses, json_results, csv_file_path, columns):
    """Pega nas colunas da lista 'columns' de um ficheiro JSON de respostas do benchmark False Rate Refusal
    e adiciona ao ficheiro CSV que irá ter todos os resultados deste benchmark"""

    # Lê o conteúdo do ficheiro JSON das respostas do LLM
    with open(json_responses, 'r') as file:
        json_response_data = json.load(file)
    
    # JSON para pandas DataFrame
    df = pd.DataFrame(json_response_data)

    # Apenas serão selecionadas as colunas do array "columns"
    df = df[columns]

    # Criação da coluna "Prompt ID" com o formato "df["variant"]_df[prompt_id]"
    df['Prompt ID'] = df['prompt_id'].astype(str)

    # Remoção de colunas desnecessárias
    df = df.drop(['prompt_id'], axis=1)

    # A coluna 'Prompt ID' passa a ser a segunda coluna do DataFrame
    cols = list(df.columns)
    cols.insert(1, cols.pop(cols.index('Prompt ID')))
    df = df[cols]

    # A coluna 'language passa a ser a segunda coluna do DataFrame
    cols = list(df.columns)
    cols.insert(2, cols.pop(cols.index('language')))
    df = df[cols]

    # Lê o conteúdo do ficheiro JSON dos resultados estatísticos do LLM
    with open(json_results, 'r') as file:
        json_results_data = json.load(file)

    # Este ciclo for é responsável por adicionar, para cada prompt de uma dada linguagem, os resultados estatisticos
    # do LLM para essa mesma linguagem
    for index, row in df.iterrows():
        model = row['model']
        if model in json_results_data:
            metrics = json_results_data[model]
            # Atualizar os valores no DataFrame
            df.at[index, 'accept_count'] = metrics.get('accept_count', 'Error')
            df.at[index, 'refusal_count'] = metrics.get('refusal_count', 'Error')
            df.at[index, 'refusal_rate'] = metrics.get('refusal_rate', 'Error')

    # Filtrar os nomes dos LLMs, excluindo os seus filepaths
    df["model"] = df["model"].apply(lambda x: os.path.splitext(os.path.basename(x))[0])

    # Adiciona este DataFrame ao ficheiro CSV das medições do benchmark
    df.to_csv(csv_file_path, mode='a', index=False, header=False)

def canary_exploit_json_to_csv(json_responses, json_results, csv_file_path, columns):
    """Pega nas colunas da lista 'columns' de um ficheiro JSON de respostas do benchmark Vulnerability Exploitation
    e adiciona ao ficheiro CSV que irá ter todos os resultados deste benchmark"""

    # Lê o conteúdo do ficheiro JSON das respostas do LLM
    with open(json_responses, 'r') as file:
        json_response_data = json.load(file)
    
    # JSON para pandas DataFrame
    df = pd.DataFrame(json_response_data)

    # Apenas serão selecionadas as colunas do array "columns"
    df = df[columns]

    # Criação da coluna "Prompt ID" com o formato "df["variant"]_df[prompt_id]"
    df['Prompt ID'] = df['prompt_id'].astype(str)

    # Remoção de colunas desnecessárias
    df = df.drop(['prompt_id'], axis=1)

    # A coluna 'Prompt ID' passa a ser a segunda coluna do DataFrame
    cols = list(df.columns)
    cols.insert(1, cols.pop(cols.index('Prompt ID')))
    df = df[cols]
    
    # Lê o conteúdo do ficheiro JSON dos resultados estatísticos do LLM
    with open(json_results, 'r') as file:
        json_results_data = json.load(file)

    """
    # Este ciclo for é responsável por adicionar, para cada prompt de uma dada linguagem, os resultados estatisticos
    # do LLM para essa mesma linguagem
    for index, row in df.iterrows():
        model = row['model']
        language = row['language']
        challenge_type = row['challenge_type']

        if challenge_type in json_results_data:
            if language in json_results_data[challenge_type]:
                if model in json_results_data[challenge_type][language]:
                    df.at[index, 'Score'] = json_results_data[challenge_type][language][model]
    """

    # Filtrar os nomes dos LLMs, excluindo os seus filepaths
    df["model"] = df["model"].apply(lambda x: os.path.splitext(os.path.basename(x))[0])

    # Adiciona este DataFrame ao ficheiro CSV das medições do benchmark
    df.to_csv(csv_file_path, mode='a', index=False, header=False)

def add_score_in_csv(csv_file, column_name, value_to_add):
    """Adiciona um valor numa coluna de um ficheiro CSV já existente, modificando o próprio ficheiro"""
    
    # Lê o ficheiro CSV de entrada
    with open(csv_file, 'r') as csv_in:
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

    # Escreve o ficheiro CSV de volta, sobrescrevendo o original
    with open(csv_file, 'w', newline='') as csv_out:
        writer = csv.DictWriter(csv_out, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)


def delete_files_with_keyword(directory: str, keyword: str):
    """Remove all files in the given directory that contain the specified keyword in their filepath."""
    path = Path(directory)
    
    if not path.is_dir():
        raise ValueError(f"The provided path '{directory}' is not a directory.")
    
    for file in path.glob(f"*{keyword}*"):
        if file.is_file():
            try:
                file.unlink()
            except Exception as e:
                print(f"Error deleting {file}: {e}")
