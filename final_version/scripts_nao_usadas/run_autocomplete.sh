python3 -m CybersecurityBenchmarks.benchmark.run \
   --benchmark=autocomplete \
   --prompt-path="$DATASETS/autocomplete/autocomplete.json" \
   --response-path="$DATASETS/autocomplete_responses.json" \
   --stat-path="$DATASETS/autocomplete_stat.json" \
   --llm-under-test="LLAMACPP::llama_c++/models/llama-2-7b.Q2_K.gguf::llm_1" --llm-under-test="LLAMACPP::llama_c++/models/llama-2-7b.Q3_K_L.gguf::llm_2" 
