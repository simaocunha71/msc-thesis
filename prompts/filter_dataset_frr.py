import json
import re
import argparse
from collections import defaultdict

def extract_language(prompt):
    # Extract the language from the mutated_prompt field using a regex pattern
    match = re.search(r'Generate a (\w+)', prompt)
    return match.group(1) if match else None

def filter_by_language(input_file, output_file, N):
    # Open the input file
    with open(input_file, 'r') as infile:
        data = json.load(infile)
    
    # Dictionary to store the first N entries per language category
    language_entries = defaultdict(list)
    
    # Iterate over each entry in the JSON
    for entry in data:
        # Extract the language from the mutated_prompt field
        language = extract_language(entry['mutated_prompt'])
        
        # If a language was found, and we don't have N entries for this language yet, add the entry
        if language and len(language_entries[language]) < N:
            language_entries[language].append(entry)
    
    # Compile the results into a final list
    result = []
    for entries in language_entries.values():
        result.extend(entries)
    
    # Write the result to the output file
    with open(output_file, 'w') as outfile:
        json.dump(result, outfile, indent=4)
    
    print(f"Successfully filtered the first {N} entries per language. Saved to '{output_file}'.")

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Filter the first N entries per parsed language from 'mutated_prompt'.")
    
    # Define the expected arguments
    parser.add_argument('input_file', type=str, help='Path to the input JSON file.')
    parser.add_argument('output_file', type=str, help='Path to the output JSON file.')
    parser.add_argument('N', type=int, help='Number of entries per language.')
    
    # Parse the provided arguments
    args = parser.parse_args()
    
    # Call the function with the provided arguments
    filter_by_language(args.input_file, args.output_file, args.N)

if __name__ == '__main__':
    main()

"""

python3 filter_dataset_frr.py cyberseceval/frr/frr.json cyberseceval/frr/frr_adapted.json 2

"""