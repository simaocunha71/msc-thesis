#!/bin/bash

# SETUP SCRIPT
N_TIMES=1
N_TOKENS=124
models=(
    "models/llama-2-7b.Q2_K.gguf"
)
prompts_filepath="../rapl_tests/rapl_c_function/p_back.jsonl"
RESULT_CSV="../rapl_tests/rapl_c_function/result_rapl_c.csv"

cd RAPL/
make 
cd ../../../llama_cpp/

for model in "${models[@]}"; do
    while IFS= read -r line; do
        task_id=$(echo "$line" | jq -r '.task_id')
        prompt=$(echo "$line" | jq -r '.prompt')

        # You can customize the command as needed
        sudo ../rapl_tests/rapl_c_function/RAPL/main "./main -m $model -p \"$prompt\" -n $N_TOKENS -e $N_TIMES \"$task_id\""
    done < "$prompts_filepath"

    cat "${TAG}.J" >> "$RESULT_CSV"
done

# Clean up duplicate rows in the CSV file
awk -F',' '!seen[$1, $2, $3, $4, $5, $6]++' "$RESULT_CSV" > temp && mv temp "$RESULT_CSV"

# Cleanup
rm *.J *.log

cd ../rapl_tests/rapl_c_function/RAPL/
make clean
cd ..
