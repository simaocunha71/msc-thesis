#!/bin/bash

# SETUP SCRIPT
N_TIMES=1
N_TOKENS=124
models=(
    "models/llama-2-7b.Q2_K.gguf"
)

prompts_filepath="../rapl_tests/rapl_c_function/prompts/teste.jsonl"
#prompts_filepath="../rapl_tests/rapl_c_function/prompts/prompts.jsonl"

RESULT_CSV="../rapl_tests/rapl_c_function/result_rapl_c.csv"

# Updates all the prompts so we can use in the command line
python3 handle_prompts.py "prompts/$(basename "$prompts_filepath")"



cd RAPL/
make 
cd ../../../llama_cpp/

for model in "${models[@]}"; do
    while IFS= read -r line; do
        task_id=$(echo "$line" | jq -r '.task_id')
        prompt=$(echo "$line" | jq -r '.prompt')

        # Replace "/" with "_"
        task_id_modified=${task_id//\//_}

        # You can customize the command as needed
        sudo ../rapl_tests/rapl_c_function/RAPL/main "./main -m $model -p \"$prompt\" -n $N_TOKENS -e" $N_TIMES $task_id_modified
    done < "$prompts_filepath"

    cat *.J >> "$RESULT_CSV"
done

# Clean up duplicate rows in the CSV file
awk -F',' '!seen[$1, $2, $3, $4, $5, $6]++' "$RESULT_CSV" > temp && mv temp "$RESULT_CSV"

# Cleanup
sudo rm *.J *.log

cd ../rapl_tests/rapl_c_function/RAPL/
make clean
cd ..
