#!/bin/bash
#SBATCH --job-name=mbpp
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --account=debug


source ../env/bin/activate
module load Python/3.9.6-GCCcore-11.2.0-bare
module load CMake/3.22.1-GCCcore-11.2.0

export PYTHONPATH=$PYTHONPATH:$(pwd)
export PATH=$PATH:/home/ldap/simaocunha71/.local/bin
export WEGGLI_PATH=weggli
export PATH="$HOME/.cargo/bin:$PATH"

srun python3 main.py \
    --llm_path llms/llama_c++/models/llama-2-7b.Q2_K.gguf \
    --benchmarks cyberseceval/interpreter\
    --max_tokens 512 \
    --n_ctx 4098 \
    --seed 42 \
    --n_times 1 \
    --sleep_time 1.0 \
    --save_output no \
    --shot_prompting 1 \
    --samples_interval 1
deactivate

find . -maxdepth 1 -type d -name '*pymp*' -exec rm -r {} +