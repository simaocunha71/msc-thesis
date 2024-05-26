#!/bin/bash
#SBATCH --job-name=mbpp_short
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --account=debug

module load Python/3.9.6-GCCcore-11.2.0-bare
export PYTHONPATH=$PYTHONPATH:$(pwd)

source ../thesis_env/bin/activate

#srun python3 llms/llamacpp_wrapper.py 'Mbpp/2' 'temp_prompt.txt' 'results/mbpp/mbpp.csv' 'llms/llama_c++/models/llama-2-7b.Q2_K.gguf' 512 'mbpp'
srun python3 main.py \
    --llm_path llms/llama_c++/models/llama-2-7b.Q2_K.gguf \
    --benchmarks mbpp \
    --max_tokens 512
deactivate
