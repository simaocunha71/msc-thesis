#!/bin/bash
#SBATCH --job-name=mbpp_sanitized
#SBATCH --time=3-00:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --account=debug


source ../env/bin/activate
module load Python/3.9.6-GCCcore-11.2.0-bare
module load CMake/3.22.1-GCCcore-11.2.0
export PYTHONPATH=$PYTHONPATH:$(pwd)

srun python3 main.py \
    --llm_path llms/llama_c++/models/llama-2-7b.Q2_K.gguf \
    --benchmarks mbpp \
    --max_tokens 512 \
    --n_ctx 4098 \
    --seed 42 \
    --n_times 1 \
    --save_output yes \
    --samples_interval 0-0 \
    --enable_sanitize no

deactivate
