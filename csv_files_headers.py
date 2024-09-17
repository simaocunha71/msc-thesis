import sys

def set_csv_headers(benchmarks, shot_prompting, pass_k):
    def generate_headers(base_columns, additional_columns=None):
        if additional_columns is None:
            additional_columns = []
        return base_columns + additional_columns
    
    def add_pass_k_columns(pass_k, base_names):
        columns = []
        
        # Verificação para garantir que pass_k é um número inteiro
        if not isinstance(pass_k, int):
            print(f"[ERROR] pass@k value must be an integer. Received: {pass_k}")
            sys.exit(1)
        
        # Verificação para garantir que pass_k está dentro do intervalo suportado
        if pass_k < 1 or pass_k > 100:
            print(f"[ERROR] pass@k value (k={pass_k}) not supported - only supported 1 <= pass@k <= 100")
            sys.exit(1)
        
        # Adicionar colunas baseadas em pass_k
        if pass_k == 1:
            columns += [f"{name}@1" for name in base_names]
        elif pass_k == 10:
            columns += [f"{name}@1" for name in base_names]
            columns += [f"{name}@10" for name in base_names]
        elif pass_k == 100:
            columns += [f"{name}@1" for name in base_names]
            columns += [f"{name}@10" for name in base_names]
            columns += [f"{name}@100" for name in base_names]
    
        return columns
    
    base_energy_columns = [
        "Execution time (s)", "CPU Energy (J)", "RAM Energy (J)", "GPU Energy (J)", 
        "CPU Power (W)", "RAM Power (W)", "GPU Power (W)", "CO2 emissions (Kg)", 
        "CO2 emissions rate (Kg/s)"
    ]
    
    humaneval_x_columns = add_pass_k_columns(pass_k, ["Pass"])
    mbpp_columns = add_pass_k_columns(pass_k, ["MBPP (unsanitized) pass", "MBPP+ (unsanitized) pass", "MBPP (sanitized) pass", "MBPP+ (sanitized) pass"])
    
    headers_map = {
        "humaneval_x": generate_headers(
            ["LLM", "Benchmark prompt"], 
            base_energy_columns + humaneval_x_columns + ["GoogleBLEU", "CodeBLEU", "SacreBLEU"]
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
            base_energy_columns + mbpp_columns + ["GoogleBLEU (unsanitized)", "CodeBLEU (unsanitized)", "SacreBLEU (unsanitized)",
                                                  "GoogleBLEU (sanitized)", "CodeBLEU (sanitized)", "SacreBLEU (sanitized)"]
        )
    }
    
    csv_files = {}
    
    for benchmark in benchmarks:
        for key, headers in headers_map.items():
                        # Verificar se é "autocomplete" ou "instruct" e mapear para "instruct_and_autocomplete"
            if benchmark in ["cyberseceval/autocomplete", "cyberseceval/instruct"]:
                key = benchmark.replace("cyberseceval/", "")
            
            if key in benchmark:
                # Se for um dos benchmarks "frr", "mitre", ou "interpreter", não adicionar o sufixo "_{shot_prompting}_shot"
                if key in ["frr", "mitre", "interpreter"]:
                    csv_key = f"{key}"
                if key == "autocomplete" or "instruct":
                    csv_key = f"instruct_and_autocomplete"
                else:
                    csv_key = f"{key}_{shot_prompting}_shot"
                csv_files[csv_key] = headers

        # Handle special case for 'all'
        if "all" in benchmark:
            for key, headers in headers_map.items():
                # Mesmo tratamento para o "all"
                if key in ["frr", "mitre", "interpreter"]:
                    csv_key = f"{key}"
                else:
                    csv_key = f"{key}_{shot_prompting}_shot"
                csv_files[csv_key] = headers

    return csv_files
