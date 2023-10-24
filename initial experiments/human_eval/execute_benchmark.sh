#!/bin/bash

#python3 get_samples.py data/problems_llama-2-7b.Q2_K.jsonl

python3 evaluate_functional_correctness.py data/samples_llama-2-7b.Q2_K.jsonl --problem_file=data/problems_llama-2-7b.Q2_K.jsonl
