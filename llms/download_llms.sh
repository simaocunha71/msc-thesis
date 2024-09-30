#!/bin/bash

# Define a target directory for downloading models
MODEL_DIR="models"

# Create the models directory if it doesn't exist
mkdir -p "$MODEL_DIR"

# Change into the models directory
cd "$MODEL_DIR" || exit

# Download the models from Hugging Face
wget https://huggingface.co/bartowski/codegeex4-all-9b-GGUF/resolve/main/codegeex4-all-9b-Q6_K_L.gguf
wget https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF/resolve/main/codellama-7b-instruct.Q5_K_M.gguf
wget https://huggingface.co/TheBloke/deepseek-coder-6.7B-instruct-GGUF/resolve/main/deepseek-coder-6.7b-instruct.Q5_K_M.gguf
wget https://huggingface.co/bartowski/Meta-Llama-3-8B-Instruct-GGUF/resolve/main/Meta-Llama-3-8B-Instruct-Q6_K.gguf
wget https://huggingface.co/TheBloke/Starling-LM-7B-alpha-GGUF/resolve/main/starling-lm-7b-alpha.Q5_K_S.gguf
wget https://huggingface.co/DavidAU/Tess-10.7B-v2.0-Q6_K-GGUF/resolve/main/tess-10.7b-v2.0.Q6_K.gguf
wget https://huggingface.co/TheBloke/Orca-2-13B-GGUF/resolve/main/orca-2-13b.Q3_K_M.gguf

# Return to the previous directory
cd ..
