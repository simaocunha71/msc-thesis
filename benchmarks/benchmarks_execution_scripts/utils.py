import csv
import pandas as pd
import json, os
from pathlib import Path

def autocompleteOrInstruct_json_to_csv(json_responses: str, json_results: str, csv_file_path: str, columns: list) -> None:
    """
    Extracts columns from a JSON file of responses from the Autocomplete or Instruct benchmark
    and appends the data to a specified CSV file containing results of this benchmark.

    Args:
        json_responses (str): The path to the JSON file containing responses from the LLM.
        json_results (str): The path to the JSON file containing statistical results from the LLM.
        csv_file_path (str): The path to the CSV file where results will be stored.
        columns (list): A list of columns to extract from the JSON responses.
    """
    # Read the content of the JSON file containing LLM responses
    with open(json_responses, 'r') as file:
        json_response_data = json.load(file)

    # Convert JSON to pandas DataFrame
    df = pd.DataFrame(json_response_data)

    # Select only the specified columns
    df = df[columns]

    df['Variant'] = df['variant'].astype(str)
    df['Prompt ID'] = df['prompt_id'].astype(str)

    # Remove unnecessary columns
    df = df.drop(['variant', 'prompt_id'], axis=1)

    # Reorder columns to place 'Prompt ID' as the second column
    cols = list(df.columns)
    cols.insert(1, cols.pop(cols.index('Prompt ID')))
    cols.insert(2, cols.pop(cols.index('Variant')))
    df = df[cols]

    # Read the content of the JSON file containing statistical results
    with open(json_results, 'r') as file:
        json_results_data = json.load(file)

    # Loop to add statistical results for each prompt in a given language
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

    # Filter the names of the LLMs, excluding their file paths
    df["model"] = df["model"].apply(lambda x: os.path.splitext(os.path.basename(x))[0])

    # Append this DataFrame to the CSV file of benchmark measurements
    df.to_csv(csv_file_path, mode='a', index=False, header=False)


def mitre_json_to_csv(json_responses: str, json_results: str, csv_file_path: str, columns: list) -> None:
    """
    Extracts columns from a JSON file of responses from the MITRE benchmark
    and appends the data to a specified CSV file containing results of this benchmark.

    Args:
        json_responses (str): The path to the JSON file containing responses from the LLM.
        json_results (str): The path to the JSON file containing statistical results from the LLM.
        csv_file_path (str): The path to the CSV file where results will be stored.
        columns (list): A list of columns to extract from the JSON responses.
    """
    # Read the content of the JSON file containing LLM responses
    with open(json_responses, 'r') as file:
        json_response_data = json.load(file)

    # Convert JSON to pandas DataFrame
    df = pd.DataFrame(json_response_data)

    # Select only the specified columns
    df = df[columns]

    # Create the "Prompt ID" column in the format "df['variant']_df[prompt_id]"
    df['Prompt ID'] = df['prompt_id'].astype(str)

    # Remove unnecessary columns
    df = df.drop(['prompt_id'], axis=1)

    # Reorder columns to place 'Prompt ID' as the second column
    cols = list(df.columns)
    cols.insert(1, cols.pop(cols.index('Prompt ID')))
    df = df[cols]

    # Read the content of the JSON file containing statistical results
    with open(json_results, 'r') as file:
        json_results_data = json.load(file)

    # Loop to add statistical results for each prompt in a given language
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

    # Filter the names of the LLMs, excluding their file paths
    df["model"] = df["model"].apply(lambda x: os.path.splitext(os.path.basename(x))[0])

    # Append this DataFrame to the CSV file of benchmark measurements
    df.to_csv(csv_file_path, mode='a', index=False, header=False)


def interpreter_json_to_csv(json_responses: str, json_results: str, csv_file_path: str, columns: list) -> None:
    """
    Extracts columns from a JSON file of responses from the Interpreter benchmark
    and appends the data to a specified CSV file containing results of this benchmark.

    Args:
        json_responses (str): The path to the JSON file containing responses from the LLM.
        json_results (str): The path to the JSON file containing statistical results from the LLM.
        csv_file_path (str): The path to the CSV file where results will be stored.
        columns (list): A list of columns to extract from the JSON responses.
    """
    # Read the content of the JSON file containing LLM responses
    with open(json_responses, 'r') as file:
        json_response_data = json.load(file)

    # Convert JSON to pandas DataFrame
    df = pd.DataFrame(json_response_data)

    # Select only the specified columns
    df = df[columns]

    # Read the content of the JSON file containing statistical results
    with open(json_results, 'r') as file:
        json_results_data = json.load(file)

    # Expand rows where "attack_type" contains multiple values
    expanded_rows = []
    for _, row in df.iterrows():
        if isinstance(row['attack_type'], list):
            attack_types = row['attack_type']
        else:
            attack_types = row['attack_type'].split('|')
        for attack_type in attack_types:
            new_row = row.copy()
            # Add the value of prompt_id to attack_type
            new_row['attack_type'] = f"{attack_type}"
            expanded_rows.append(new_row)

    df = pd.DataFrame(expanded_rows)

    # Add statistical results for each row
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

    # Filter the names of the LLMs, excluding their file paths
    df["model"] = df["model"].apply(lambda x: os.path.splitext(os.path.basename(x))[0])

    # Append this DataFrame to the CSV file of benchmark measurements
    df.to_csv(csv_file_path, mode='a', index=False, header=False)


def frr_json_to_csv(json_responses: str, json_results: str, csv_file_path: str, columns: list) -> None:
    """
    Extracts columns from a JSON file of responses from the False Rate Refusal benchmark
    and appends the data to a specified CSV file containing results of this benchmark.

    Args:
        json_responses (str): The path to the JSON file containing responses from the LLM.
        json_results (str): The path to the JSON file containing statistical results from the LLM.
        csv_file_path (str): The path to the CSV file where results will be stored.
        columns (list): A list of columns to extract from the JSON responses.
    """
    # Read the content of the JSON file containing LLM responses
    with open(json_responses, 'r') as file:
        json_response_data = json.load(file)

    # Convert JSON to pandas DataFrame
    df = pd.DataFrame(json_response_data)

    # Select only the specified columns
    df = df[columns]

    # Create the "Prompt ID" column with the format "df["variant"]_df[prompt_id]"
    df['Prompt ID'] = df['prompt_id'].astype(str)

    # Remove unnecessary columns
    df = df.drop(['prompt_id'], axis=1)

    # Move 'Prompt ID' to the second column of the DataFrame
    cols = list(df.columns)
    cols.insert(1, cols.pop(cols.index('Prompt ID')))
    df = df[cols]

    # Move 'language' to the second column of the DataFrame
    cols = list(df.columns)
    cols.insert(2, cols.pop(cols.index('language')))
    df = df[cols]

    # Read the content of the JSON file containing statistical results
    with open(json_results, 'r') as file:
        json_results_data = json.load(file)

    # Add statistical results for each row
    for index, row in df.iterrows():
        model = row['model']
        if model in json_results_data:
            metrics = json_results_data[model]
            # Update the values in the DataFrame
            df.at[index, 'accept_count'] = metrics.get('accept_count', 'Error')
            df.at[index, 'refusal_count'] = metrics.get('refusal_count', 'Error')
            df.at[index, 'refusal_rate'] = metrics.get('refusal_rate', 'Error')

    # Filter the names of the LLMs, excluding their file paths
    df["model"] = df["model"].apply(lambda x: os.path.splitext(os.path.basename(x))[0])

    # Append this DataFrame to the CSV file of benchmark measurements
    df.to_csv(csv_file_path, mode='a', index=False, header=False)


def canary_exploit_json_to_csv(json_responses: str, json_results: str, csv_file_path: str, columns: list):
    """
    Extracts specified columns from a JSON file containing responses from the Vulnerability Exploitation benchmark
    and appends the data to a specified CSV file that contains results of this benchmark.

    Args:
        json_responses (str): The path to the JSON file containing responses from the LLM.
        json_results (str): The path to the JSON file containing statistical results from the LLM.
        csv_file_path (str): The path to the CSV file where results will be stored.
        columns (list): A list of columns to extract from the JSON responses.
    """

    # Read the content of the JSON file containing LLM responses
    with open(json_responses, 'r') as file:
        json_response_data = json.load(file)
    
    # Convert JSON to pandas DataFrame
    df = pd.DataFrame(json_response_data)

    # Only select the columns from the "columns" array
    df = df[columns]

    # Create the "Prompt ID" column in the format "df['variant']_df[prompt_id]"
    df['Prompt ID'] = df['prompt_id'].astype(str)

    # Remove unnecessary columns
    df = df.drop(['prompt_id'], axis=1)

    # Move the 'Prompt ID' column to be the second column in the DataFrame
    cols = list(df.columns)
    cols.insert(1, cols.pop(cols.index('Prompt ID')))
    df = df[cols]
    
    # Read the content of the JSON file containing statistical results from the LLM
    with open(json_results, 'r') as file:
        json_results_data = json.load(file)

    
    # This for loop is responsible for adding, for each prompt of a given language, the statistical results
    # from the LLM for that same language
    for index, row in df.iterrows():
        model = row['model']
        language = row['language']
        challenge_type = row['challenge_type']

        if challenge_type in json_results_data:
            if language in json_results_data[challenge_type]:
                if model in json_results_data[challenge_type][language]:
                    df.at[index, 'Score'] = json_results_data[challenge_type][language][model]
    

    # Filter the names of the LLMs, excluding their file paths
    df["model"] = df["model"].apply(lambda x: os.path.splitext(os.path.basename(x))[0])

    # Append this DataFrame to the CSV file for benchmark measurements
    df.to_csv(csv_file_path, mode='a', index=False, header=False)


def add_score_in_csv(csv_file: str, column_name: str, value_to_add) -> None:
    """
    Adds a value to a specified column in an existing CSV file, modifying the file itself.

    Args:
        csv_file (str): The path to the CSV file to be modified.
        column_name (str): The name of the column to which the value will be added.
        value_to_add (Any): The value to add to the specified column.

    Raises:
        ValueError: If the specified column does not exist in the input CSV file.

    """
    with open(csv_file, 'r') as csv_in:
        reader = csv.DictReader(csv_in)
        header = reader.fieldnames

        # Check if the column to which we want to add the score exists in the input CSV file
        if column_name not in header:
            raise ValueError(f"The column '{column_name}' does not exist in the input CSV file.")

        # Read all rows and fill the specified column with the given score value
        rows = list(reader)
        for row in rows:
            if column_name not in row or not row[column_name]:
                row[column_name] = value_to_add

    # Write the CSV file back, overwriting the original
    with open(csv_file, 'w', newline='') as csv_out:
        writer = csv.DictWriter(csv_out, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)


def delete_files_with_keyword(directory: str, keyword: str) -> None:
    """
    Removes all files in the given directory that contain the specified keyword in their filepath.

    Args:
        directory (str): The directory from which files will be deleted.
        keyword (str): The keyword to search for in the file paths.

    Raises:
        ValueError: If the provided path is not a directory.
    """
    path = Path(directory)
    
    if not path.is_dir():
        raise ValueError(f"The provided path '{directory}' is not a directory.")
    
    for file in path.glob(f"*{keyword}*"):
        if file.is_file():
            try:
                file.unlink()
            except Exception as e:
                print(f"Error deleting {file}: {e}")
