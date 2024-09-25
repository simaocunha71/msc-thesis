import sys

def set_csv_headers(benchmarks, pass_k):
    def generate_headers(base_columns, additional_columns=None):
        """Generate headers by concatenating base and additional columns."""
        return base_columns + (additional_columns or [])
    
    def add_pass_k_columns(pass_k, base_names):
        """Generate pass@k columns based on the value of pass_k."""
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
            base_energy_columns + [
                "Maliciousness Level", "Is extremely malicious", 
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

        mapped_benchmark = benchmark.replace("cyberseceval/", "") if "cyberseceval" in benchmark else benchmark
        key = "instruct_and_autocomplete" if mapped_benchmark in ["autocomplete", "instruct"] else mapped_benchmark
        
        if key in headers_map:
            csv_files[key] = headers_map[key]
        
        if "all" in benchmark:
            # Special handling for "all" benchmarks
            for key, headers in headers_map.items():
                csv_files[key] = headers

    return csv_files
