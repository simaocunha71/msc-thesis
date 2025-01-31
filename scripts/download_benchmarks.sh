#!/bin/bash

# Save the current directory
current_dir=$(pwd)

# Navigate to the benchmarks directory
cd ../benchmarks || exit

# Download HumanEval-X benchmark [URL anonymized]
git clone https://anonymous.4open.science/r/codefuse-evaluation-2D67

# Download MBPP and MBPP+ benchmarks [URL anonymized]
git clone https://anonymous.4open.science/r/evalplus-2C5C

# Download CyberSecEval benchmark [URL anonymized]
git clone https://anonymous.4open.science/r/PurpleLlama-2766

# Return to the original directory
cd "$current_dir" || exit
