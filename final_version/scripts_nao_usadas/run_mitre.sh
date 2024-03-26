python3 -m CybersecurityBenchmarks.benchmark.run \
   --benchmark=mitre \
   --prompt-path="prompts/cyberseceval/mitre_benchmark_100_per_category_with_augmentation.json" \
   --response-path="prompts/cyberseceval/mitre_responses.json" \
   --judge-response-path="prompts/cyberseceval/mitre_judge_responses.json" \
   --stat-path="prompts/cyberseceval/mitre_stat.json" \
   --judge-llm="LLAMACPP::llama_c++/models/llama-2-7b.Q3_K_L.gguf::llm_2" \
   --expansion-llm="LLAMACPP::llama_c++/models/llama-2-7b.Q3_K_S.gguf::llm_3" \
   --llm-under-test="LLAMACPP::llama_c++/models/llama-2-7b.Q2_K.gguf::llm_1"