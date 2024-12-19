### Master's Dissertation in Informatics Engineering (2023/2024)
#### Towards a Platform for Benchmarking Large Language Models

This repository contains all the work done for my Master's Dissertation in Informatics Engineering: the tool to evaluate LLMs and measure metrics such as CPU energy consumption and execution time during the outputs generation. This CLI application also evaluates the quality and functionality of the generated code by benchmarking LLMs such as HumanEval-X, MBPP+ and CyberSecEval.

| Documents                            | Link                                                                 |
|-------------------------------------|----------------------------------------------------------------------|
| Dissertation                        | [dissertation.pdf](https://simaocunha71.github.io/assets/docs/msc-thesis/dissertation.pdf) |
| Thesis Presentation                    | [presentation.pdf](https://simaocunha71.github.io/assets/docs/msc-thesis/presentation.pdf) |
| Pre-Dissertation Report (PDR)                                  | [rpd.pdf](https://simaocunha71.github.io/assets/docs/msc-thesis/pdr.pdf)       |
| PDR Presentation                    | [pdr_presentation.pdf](https://simaocunha71.github.io/assets/docs/msc-thesis/pdr_presentation.pdf) |

#### Pre-requisites

- **Python 3.9** or newer (mandatory)
- **Docker** (mandatory)
- **CMake** (mandatory)
- **cargo** (mandatory)
- **Debian-based Linux distributions**, such as Ubuntu (recommended)
- **Intel CPU** (highly recommended)
- Install **weggli**:

```bash
cargo install weggli --rev=9d97d462854a9b682874b259f70cc5a97a70f2cc --git=https://github.com/weggli-rs/weggli
```

To facilitate the installation of the pre-requisites, you can execute the following script, which installs the exact versions used in the dissertation. However, installing these specific versions is not mandatory:

```bash
bash scripts/install_prerequisites.sh
```

#### Dependencies

1. Install all Python libraries listed in `requirements.txt` using a virtual environment (e.g., named `env`):

```bash
# Create a virtual environment named 'env'
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install the required Python libraries
pip3 install -r requirements.txt
```

For `llama-cpp-python` installation with CPU support (used in this dissertation), execute:

```bash
CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip3 install llama-cpp-python
```

For other hardware acceleration backends, refer to the [llama-cpp-python documentation](https://github.com/abetlen/llama-cpp-python?tab=readme-ov-file#installation-configuration):

2. Download the benchmark repositories for HumanEval-X, MBPP+ and CyberSecEval:

```bash
bash scripts/download_benchmarks.sh
```

2.1. Pull the Docker image required for calculating pass@k (where k = 1, 10, or 100):

```bash
docker pull registry.cn-hangzhou.aliyuncs.com/codefuse/codefuseeval:latest
```

3. Download the LLMs used in the dissertation:

```bash
bash scripts/download_llms.sh
```

4. Download the benchmark dataset files used in the dissertation:

```bash
bash scripts/download_prompt_files.sh
```

5. Download results, sample files and model generations:

```bash
wget https://github.com/simaocunha71/msc-thesis/releases/download/v1.0.0/msc_results.zip
bash scripts/msc_results.sh decompress
```

#### Repository structure

- *benchmarks/*: Contains repositories used for LLMs benchmarking.
- *data_analysis/*: Jupyter Notebooks for analyzing results from the dissertation.
- *llms/*: Python class to execute LLMs and the quantized model files (stored in `llms/models/`).
- *prompts/*: Benchmark datasets used in the dissertation.

#### Contributing to the Repository

- **Adding Support for Additional Frameworks:** Refer to the instructions in [`llms/README.md`](llms/README.md) for guidance on integrating new frameworks for LLM execution.  
- **Adding New Benchmarks:** Follow the steps outlined in [`benchmarks/README.md`](benchmarks/README.md) to include additional benchmarks in the repository.  


#### Execute the program

To execute the program, you should execute the `main.py` file, which arguments are:

- **`--llm_path`**: Path(s) to the LLM(s) to execute. This argument is required.
- **`--benchmarks`**: Benchmarks to run. The available options are:

    - **`humaneval_x`**
    - **`humaneval_x/c++`**
    - **`humaneval_x/javascript`**
    - **`humaneval_x/python`**
    - **`humaneval_x/go`**
    - **`humaneval_x/java`**

    ---
    
    - **`cyberseceval`**
    - **`cyberseceval/autocomplete`**
    - **`cyberseceval/instruct`**
    - **`cyberseceval/mitre`**
    - **`cyberseceval/frr`**
    - **`cyberseceval/interpreter`**
    - **`cyberseceval/canary_exploit`**

    ---
    
    - **`mbpp`**

    This argument is required. Users may select any combination of benchmarks, but a validation step ensures that all selected benchmarks belong to the same category (which are `humanevalx`, `mbpp`, and `cyberseceval`). For example, selecting `humaneval_x/c++` and `humaneval_x/java` is valid, whereas combining `humaneval_x` with `mbpp` or `cyberseceval` is invalid.

- **`--max_tokens`**: The maximum number of tokens the LLM will use to generate responses. The default value is 512.
- **`--n_ctx`**: The maximum number of tokens the LLM considers when processing the context of a response. The default value is 512.
- **`--seed`**: The seed used to ensure reproducibility by generating the same outputs. The default value is 512.
- **`--n_times`**: The number of times to execute each prompt. The default value is 1.
- **`--save_output`**: Specifies whether to save the LLM outputs to files. Options are `yes` or `no`, with the default being `no`.
- **`--samples_interval`**: Defines the range of benchmark prompts to execute. The format is `[min]-[max]`, where `min` is the starting index (beginning at 1) and `max` is the ending index. Alternatively, `[index]` can be used to run a specific prompt, or `all` to execute the entire dataset. The default is `all`.
- **`--n_shot_prompting`**: The number of examples (shots) to include in the prompt for task demonstration. A value of 0 indicates zero-shot prompting, 1 for one-shot prompting and so on. The default value is 0.
- **`--sleep_time`**: The number of seconds to wait between executions. The default is 3.0 seconds.
- **`--pass_k`**: The maximum `k` value for the pass@k metric. The options are 1, 10, or 100, with the default set to 1.
- **`--top_p`**: The top-p value for nucleus sampling, with a default of 0.95.
- **`--temperature`**: The temperature for sampling, defaulting to 0.6.

To execute the program, run the following command, changing the parameters as needed:

```bash
#!/bin/bash

source ../env/bin/activate

export PYTHONPATH=$PYTHONPATH:$(pwd)
export WEGGLI_PATH=weggli
export PATH="$HOME/.cargo/bin:$PATH"

python3 main.py \
    --llm_path llms/models/codellama-7b-instruct.Q5_K_M.gguf \
    --benchmarks humaneval_x/\
    --max_tokens 512 \
    --n_ctx 4098 \
    --seed 42 \
    --top_p 0.95 \
    --temperature 0.6 \
    --n_times 1 \
    --sleep_time 1.0 \
    --save_output yes \
    --n_shot_prompting 0 \
    --pass_k 1 \
    --samples_interval all

deactivate
```
