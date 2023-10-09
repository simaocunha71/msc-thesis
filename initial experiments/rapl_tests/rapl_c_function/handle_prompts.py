import json
import shlex
import subprocess
import sys

def update_prompts(jsonl_filename):
    with open(jsonl_filename, 'r+') as jsonl_file:
        lines = jsonl_file.readlines()
        jsonl_file.seek(0)  # Move the file pointer to the beginning

        for line in lines:
            data = json.loads(line)

            # Extract the prompt field from the JSON data
            prompt = data.get("prompt", "")

            # Apply shlex to the prompt
            prompt_escaped = shlex.quote(prompt)

            # Update the data with the result
            data['prompt'] = prompt_escaped.strip()

            # Write the updated data back to the file
            jsonl_file.write(json.dumps(data) + '\n')

        # Truncate the file in case the new content is shorter than the old content
        jsonl_file.truncate()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage example: python3 handle_prompts.py prompts.jsonl")
        sys.exit(1)

    update_prompts(sys.argv[1])
