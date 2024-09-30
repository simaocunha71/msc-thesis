import json
import argparse
from collections import defaultdict

def filter_by_language(input_file, output_file, N):
    # Open the input file
    with open(input_file, 'r') as infile:
        data = json.load(infile)
    
    # Dictionary to store the first N entries per language category
    language_entries = defaultdict(list)
    
    # Iterate over each entry in the JSON
    for entry in data:
        language = entry['language']
        
        # Add the entry if we don't have N entries for this language yet
        if len(language_entries[language]) < N:
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
    parser = argparse.ArgumentParser(description="Filter the first N entries per language category.")
    
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

python3 filter_dataset_auto_and_instr.py cyberseceval/autocomplete/autocomplete.json cyberseceval/autocomplete/autocomplete_adapted.json 2
python3 filter_dataset_auto_and_instr.py cyberseceval/instruct/instruct.json cyberseceval/instruct/instruct_adapted.json 2

"""