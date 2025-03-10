### LLM Benchmarks and Adding New Benchmarks to the Repository

Currently, this application supports three LLM benchmarks: **HumanEval-X**, **MBPP+**, and **CyberSecEval**. The repositories for these benchmarks are listed below:

| Benchmark Repository            | Link                                                                                  |
|---------------------------------|---------------------------------------------------------------------------------------|
| **CodeFuseEval** (HumanEval-X)  | [https://github.com/simaocunha71/codefuse-evaluation](https://github.com/simaocunha71/codefuse-evaluation) |
| **EvalPlus** (MBPP+)            | [https://github.com/simaocunha71/evalplus](https://github.com/simaocunha71/evalplus)                 |
| **PurpleLlama** (CyberSecEval)  | [https://github.com/simaocunha71/PurpleLlama](https://github.com/simaocunha71/PurpleLlama)           |

#### Adding a New Benchmark

To include support for a new benchmark (e.g., `new_benchmark_repository`), follow these steps:

1. **Implement Benchmark Execution Script:**
   - Create a Python file at `benchmarks/benchmarks_execution_scripts/new_benchmark_repository.py`.
   - This script should use `os.system()` to execute a bash command for running the new benchmark.

2. **Implement Sample Saving Logic:**
   - Create a file named `get_samples_new_benchmark_repository.py`.
   - This script should save the LLM generations into a JSONL file with the following format:
     ```json
     {"task_id": "XX", "generation": "YY"}
     ```

3. **Download the Dataset:**
   - Save the dataset for the new benchmark in the directory `prompts/new_benchmark_repository/`.

4. **Update CSV Headers:**
   - Update the function `set_csv_headers` in `csv_files_headers.py` to include column headers specific to the new benchmark.

   ```python
   def set_csv_headers(benchmarks: list, pass_k: int) -> dict:
       ...
       headers_map = {
           "humaneval_x": ...,
           "new_benchmark_repository": pass
       }
   ```

5. **Update `start_measure` Function:**
   - Modify the `start_measure` function in `main.py` to integrate the new benchmark logic. 
   - Add handling for `new_benchmark_repository` in the `handle_prompt_files` sub-function.

   Example:
   ```python
   def start_measure(llm_path_list: list, prompts_filepath_list: list, max_tokens: int, n_ctx: int, 
                     seed: int, save_output_flag: str, samples_interval: str, shot_prompting: int, 
                     SLEEP_TIME: float, pass_k: int, top_p: float, temperature: float) -> None:
       ...

       def handle_prompt_files(llm_obj, llm_path, prompts_filepath, pass_k):
           ...

           if "humaneval_x" in temp_prompts_filepath:
               ...
           elif "mbpp" in temp_prompts_filepath:
               ...
           elif "new_benchmark_repository" in temp_prompts_filepath:
               pass
           else:
               print("JSONL file does not belong to any considered benchmark")
           ...
       ...
    ```
