python3 main.py \
    --llm_path llms/llama_c++/models/llama-2-7b.Q2_K.gguf \
    --benchmarks cyberseceval\
    --max_tokens 512 \
    --n_ctx 4098 \
    --seed 42 \
    --n_times 1 \
    --save_output no \
    --shot_prompting 0 \
    --samples_interval 1-1