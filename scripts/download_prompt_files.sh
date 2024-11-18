#!/bin/bash

cd ../prompts 

# Create and navigate to the humaneval_x directory
mkdir -p humaneval_x
cd humaneval_x/ || exit

# Download HumanEval-X datasets
wget "https://github.com/THUDM/CodeGeeX/raw/main/codegeex/benchmark/humaneval-x/cpp/data/humaneval_cpp.jsonl.gz"
wget "https://github.com/THUDM/CodeGeeX/raw/main/codegeex/benchmark/humaneval-x/go/data/humaneval_go.jsonl.gz"
wget "https://github.com/THUDM/CodeGeeX/raw/main/codegeex/benchmark/humaneval-x/java/data/humaneval_java.jsonl.gz"
wget "https://github.com/THUDM/CodeGeeX/raw/main/codegeex/benchmark/humaneval-x/js/data/humaneval_js.jsonl.gz"
wget "https://github.com/THUDM/CodeGeeX/raw/main/codegeex/benchmark/humaneval-x/python/data/humaneval_python.jsonl.gz"
gzip -d *.gz
cd .. || exit

# Create and navigate to the mbpp directory
mkdir -p mbpp
cd mbpp/ || exit

# Download MBPP+ dataset
wget "https://github.com/evalplus/mbppplus_release/releases/download/v0.2.0/MbppPlus.jsonl.gz"
gzip -d *.gz
cd .. || exit

# Download CyberSecEval datasets
wget https://github.com/meta-llama/PurpleLlama/archive/refs/heads/main.zip
unzip main.zip 
mv PurpleLlama-main/CybersecurityBenchmarks/datasets ./cyberseceval/
rm -rf main.zip PurpleLlama-main

cd ..