import csv
import pandas as pd
import json, os

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

    # Criação da coluna "Benchmark prompt" com o formato "df["variant"]_df[prompt_id]"
    df['Benchmark prompt'] = df['variant'] + '_' + df['prompt_id'].astype(str)

    # Remoção de colunas desnecessárias
    df = df.drop(['variant', 'prompt_id'], axis=1)

    # A coluna 'Benchmark prompt' passa a ser a segunda coluna do DataFrame
    cols = list(df.columns)
    cols.insert(1, cols.pop(cols.index('Benchmark prompt')))
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

    # Criação da coluna "Benchmark prompt" com o formato "df["variant"]_df[prompt_id]"
    df['Benchmark prompt'] = "MITRE" + '_' + df['prompt_id'].astype(str)

    # Remoção de colunas desnecessárias
    df = df.drop(['prompt_id'], axis=1)

    # A coluna 'Benchmark prompt' passa a ser a segunda coluna do DataFrame
    cols = list(df.columns)
    cols.insert(1, cols.pop(cols.index('Benchmark prompt')))
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

    """
    {
        'llms/llama_c++/models/llama-2-7b.Q2_K.gguf': {
            'Privilege Escalation': {
                'is_extremely_malicious': 0, 
                'is_potentially_malicious': 0, 
                'is_non_malicious': 0, 
                'total_count': 1.0, 
                'malicious_percentage': 1.0
            }
        }
    }

"""
    df['attack_type'] = df['attack_type'].apply(lambda x: '|'.join(x))

    # Este ciclo for é responsável por adicionar, para cada prompt de uma dada linguagem, os resultados estatisticos
    # do LLM para essa mesma linguagem
    for attack_type, model in zip((df['attack_type']), df['model']):
        if model in json_results_data:
            if attack_type in json_results_data[model]:
                metrics = json_results_data[model][attack_type]
                df.loc[df['attack_type'] == attack_type, [
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