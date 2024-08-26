#!/bin/bash
#SBATCH --job-name=deepseek_heval_cpp_0s
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
export PATH=$PATH:/home/ldap/simaocunha71/.local/bin
export WEGGLI_PATH=weggli
export PATH="$HOME/.cargo/bin:$PATH"

srun python3 main.py \
    --llm_path llms/llama_c++/models/deepseek-coder-6.7b-instruct.Q5_K_M.gguf \
    --benchmarks humaneval_x/cpp \
    --max_tokens 512 \
    --n_ctx 4098 \
    --seed 42 \
    --top_p 0.95 \
    --temperature 0.6 \
    --n_times 1 \
    --sleep_time 1.0 \
    --save_output yes \
    --n_shot_prompting 0 \
    --pass_k 10 \
    --samples_interval all


deactivate


find . -maxdepth 1 -type d -name '*pymp*' -exec rm -r {} +
find . -maxdepth 1 -type d -name '*cpp*' -exec rm -r {} +
find . -maxdepth 1 -type d -name '*go*' -exec rm -r {} +
find . -maxdepth 1 -type d -name '*java*' -exec rm -r {} +
find . -maxdepth 1 -type d -name '*js*' -exec rm -r {} +