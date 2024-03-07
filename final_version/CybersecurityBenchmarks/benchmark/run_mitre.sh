python3 -m CybersecurityBenchmarks.benchmark.run \
   --benchmark=instruct \
   --prompt-path="$DATASETS/instruct/instruct.json" \
   --response-path="$DATASETS/instruct_responses.json" \
   --stat-path="$DATASETS/instruct_stat.json" \
   --llm-under-test="LLAMACPP::llama_c++/models/llama-2-7b.Q2_K.gguf::llm_1"

python3 -m CybersecurityBenchmarks.benchmark.run \
   --benchmark=mitre \
   --prompt-path="$DATASETS/mitre/mitre_benchmark_100_per_category_with_augmentation.json" \
   --response-path="$DATASETS/mitre_responses.json" \
   --judge-response-path="$DATASETS/mitre_judge_responses.json" \
   --stat-path="$DATASETS/mitre_stat.json" \
   --judge-llm="OPENAI::gpt-3.5-turbo::<YOUR API KEY>" \
   --expansion-llm="OPENAI::gpt-3.5-turbo::<YOUR API KEY>" \
   --llm-under-test="LLAMACPP::llama_c++/models/llama-2-7b.Q2_K.gguf::llm_1"