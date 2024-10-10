import json
import argparse
from collections import defaultdict

def filter_by_attack_type(input_file, output_file, N):
    # Open the input file
    with open(input_file, 'r') as infile:
        data = json.load(infile)
    
    # Dictionary to store entries per attack_type
    attack_type_entries = defaultdict(list)
    
    # Iterate over each entry in the JSON
    for entry in data:
        attack_types = entry.get('attack_type', [])
        
        # Ensure we're working with entries that contain an attack_type
        for attack_type in attack_types:
            # Add the entry to the corresponding attack type
            attack_type_entries[attack_type].append(entry)
    
    # Compile the results, keeping only the last N entries per attack_type
    result = []
    for entries in attack_type_entries.values():
        result.extend(entries[-N:])  # Take the last N entries

    # Write the result to the output file
    with open(output_file, 'w') as outfile:
        json.dump(result, outfile, indent=4)
    
    print(f"Successfully filtered the last {N} entries per attack_type. Saved to '{output_file}'.")


def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Filter the first N entries per attack_type.")
    
    # Define the expected arguments
    parser.add_argument('input_file', type=str, help='Path to the input JSON file.')
    parser.add_argument('output_file', type=str, help='Path to the output JSON file.')
    parser.add_argument('N', type=int, help='Number of entries per attack_type.')
    
    # Parse the provided arguments
    args = parser.parse_args()
    
    # Call the function with the provided arguments
    filter_by_attack_type(args.input_file, args.output_file, args.N)

if __name__ == '__main__':
    main()

"""

python3 filter_dataset_interpreter.py cyberseceval/interpreter/interpreter.json cyberseceval/interpreter/interpreter_adapted.json 2

"""