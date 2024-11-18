#!/bin/bash

# Save the current directory
current_dir=$(pwd)

# Navigate to the benchmarks directory
cd ../benchmarks || exit

# Download HumanEval-X benchmark
git clone https://github.com/simaocunha71/codefuse-evaluation

# Download MBPP and MBPP+ benchmarks
git clone https://github.com/simaocunha71/evalplus.git

# Download CyberSecEval benchmark
git clone https://github.com/simaocunha71/PurpleLlama.git

# Return to the original directory
cd "$current_dir" || exit
