import json
import argparse
from collections import defaultdict

def filter_by_mitre_category(input_file, output_file, N):
    # Open the input file
    with open(input_file, 'r') as infile:
        data = json.load(infile)
    
    # Dictionary to store entries per mitre_category
    mitre_category_entries = defaultdict(list)
    
    # Iterate over each entry in the JSON
    for entry in data:
        mitre_category = entry.get('mitre_category')
        
        # Add the entry to the corresponding mitre_category
        if mitre_category:
            mitre_category_entries[mitre_category].append(entry)
    
    # Compile the results, keeping only the last N entries per mitre_category
    result = []
    for entries in mitre_category_entries.values():
        result.extend(entries[-N:])  # Take the last N entries

    # Write the result to the output file
    with open(output_file, 'w') as outfile:
        json.dump(result, outfile, indent=4)
    
    print(f"Successfully filtered the last {N} entries per mitre_category. Saved to '{output_file}'.")


def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Filter the first N entries per mitre_category.")
    
    # Define the expected arguments
    parser.add_argument('input_file', type=str, help='Path to the input JSON file.')
    parser.add_argument('output_file', type=str, help='Path to the output JSON file.')
    parser.add_argument('N', type=int, help='Number of entries per mitre_category.')
    
    # Parse the provided arguments
    args = parser.parse_args()
    
    # Call the function with the provided arguments
    filter_by_mitre_category(args.input_file, args.output_file, args.N)

if __name__ == '__main__':
    main()

"""

python3 filter_dataset_mitre.py cyberseceval/mitre/mitre_benchmark_100_per_category_with_augmentation.json cyberseceval/mitre/mitre_benchmark_100_per_category_with_augmentation_adapted.json 2

"""