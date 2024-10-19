import sys

def set_csv_headers(benchmarks: list, pass_k: int) -> dict:   
    """Generate headers by concatenating base columns with optional additional columns.
    Args:
        benchmarks (list): List of benchmarks to execute.
        pass_k (int): Max k value for pass@k metric.
    Returns:
        dict: Dictionary with all the CSV headers grouped by each CSV name as CSV keys.
    """

    def generate_headers(base_columns, additional_columns=None):
        """Generate headers by concatenating base columns with optional additional columns.

        Args:
            base_columns (list): A list of base column names.
            additional_columns (list, optional): A list of additional column names to concatenate. Defaults to None.

        Returns:
            list: A list containing the concatenated base and additional columns.
        """
        return base_columns + (additional_columns or [])

    
    def add_pass_k_columns(pass_k: int, base_names: list) -> list:
        """Generate pass@k columns based on the value of pass_k.

        Args:
            pass_k (int): The pass@k value, which must be between 1 and 100.
            base_names (list): A list of base column names.

        Returns:
            list: A list of pass@k columns generated from the base names.

        Raises:
            SystemExit: If pass_k is not an integer or if it is not within the supported range.
        """
        if not isinstance(pass_k, int):
            print(f"[ERROR] pass@k value must be an integer. Received: {pass_k}")
            sys.exit(1)

        if not (1 <= pass_k <= 100):
            print(f"[ERROR] pass@k value (k={pass_k}) not supported - only supported 1 <= pass@k <= 100")
            sys.exit(1)

        columns = [f"{name}@1" for name in base_names]
        if pass_k >= 10:
            columns += [f"{name}@10" for name in base_names]
        if pass_k == 100:
            columns += [f"{name}@100" for name in base_names]
        
        return columns
    
    base_energy_columns = [
        "Execution time (s)", "CPU Energy (J)", "RAM Energy (J)", "GPU Energy (J)", 
        "CPU Power (W)", "RAM Power (W)", "GPU Power (W)", "CO2 emissions (Kg)", 
        "CO2 emissions rate (Kg/s)"
    ]
    
    # Define headers based on benchmarks
    headers_map = {
        "humaneval_x": generate_headers(
            ["LLM", "Benchmark prompt"], 
            base_energy_columns + add_pass_k_columns(pass_k, ["Pass"]) + ["GoogleBLEU", "CodeBLEU", "SacreBLEU"]
        ),
        "instruct_and_autocomplete": generate_headers(
            ["LLM", "Prompt ID", "Variant", "Language"], 
            base_energy_columns + [
                "Bleu score", "Total count", "Vulnerable percentage", 
                "Vulnerable suggestion count", "Pass rate"
            ]
        ),
        "mitre": generate_headers(
            ["LLM", "Prompt ID", "Category"], 
            base_energy_columns + [
                "Refusal count", "Malicious count", "Benign count", 
                "Total count", "Benign percentage", "Else count"
            ]
        ),
        "interpreter": generate_headers(
            ["LLM", "Prompt ID", "Attack type"], 
            base_energy_columns + ["Is extremely malicious", 
                "Is potentially malicious", "Is non malicious", 
                "Total count", "Malicious percentage"
            ]
        ),
        "frr": generate_headers(
            ["LLM", "Prompt ID", "Language", "Attack type"], 
            base_energy_columns + [
                "Judge Response", "Accept count", "Refusal count", "Refusal rate"
            ]
        ),
        "canary_exploit": generate_headers(
            ["LLM", "Prompt ID", "Language", "Challenge Type"], 
            base_energy_columns + ["Score"]
        ),
        "mbpp": generate_headers(
            ["LLM", "Benchmark prompt"], 
            base_energy_columns + add_pass_k_columns(pass_k, [
                "MBPP (unsanitized) pass", "MBPP+ (unsanitized) pass", 
                "MBPP (sanitized) pass", "MBPP+ (sanitized) pass"
            ]) + [
                "GoogleBLEU (unsanitized)", "CodeBLEU (unsanitized)", "SacreBLEU (unsanitized)",
                "GoogleBLEU (sanitized)", "CodeBLEU (sanitized)", "SacreBLEU (sanitized)"
            ]
        )
    }
    
    csv_files = {}
    
    for benchmark in benchmarks:
        # Map language-specific humaneval_x benchmarks to "humaneval_x"
        if benchmark.startswith("humaneval_x/"):
            benchmark = "humaneval_x"

        # Handle benchmarks like "cyberseceval"
        mapped_benchmark = benchmark.replace("cyberseceval/", "") if "cyberseceval" in benchmark else benchmark
        key = "instruct_and_autocomplete" if mapped_benchmark in ["autocomplete", "instruct"] else mapped_benchmark
        
        if key in headers_map:
            if key in csv_files:
                # Merge headers for multiple benchmarks into the same entry
                csv_files[key] = generate_headers(csv_files[key], headers_map[key])
            else:
                csv_files[key] = headers_map[key]
        
        if "all" in benchmark:
            # Special handling for "all" benchmarks
            for key, headers in headers_map.items():
                if key in csv_files:
                    csv_files[key] = generate_headers(csv_files[key], headers)
                else:
                    csv_files[key] = headers

    return csv_files
