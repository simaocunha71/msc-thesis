def set_csv_headers(benchmarks, shot_prompting):
    # Define CSV files and their columns based on the benchmarks
    csv_files = {}

    for b in benchmarks:
        if "humaneval_x" in b:
            csv_files[f"humaneval_x_{shot_prompting}_shot"] = [
                "LLM", "Benchmark prompt", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Pass@1", "googleBLEU", "codeBLEU", "sacreBLEU"
            ]
        elif "cyberseceval/autocomplete" in b or "cyberseceval/instruct" in b:
            csv_files[f"instruct_and_autocomplete_{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Variant", "Language", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Bleu score", "Total count", "Vulnerable percentage",
                "Vulnerable suggestion count", "Pass rate"
            ]
        elif "cyberseceval/mitre" in b:
            csv_files[f"mitre_{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Category", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Refusal count", "Malicious count", "Benign count",
                "Total count", "Benign percentage", "Else count"
            ]
        elif "cyberseceval/interpreter" in b:
            csv_files[f"interpreter{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Attack type", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Maliciousness Level",
                "Is extremely malicious",
                "Is potentially malicious",
                "Is non malicious",
                "Total count",
                "Malicious percentage"
            ]
        elif "cyberseceval/frr" in b:
            csv_files[f"frr_{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Language", "Attack type", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Judge Response",
                "Accept count",
                "Refusal count",
                "Refusal rate"
            ]
        elif "cyberseceval/canary_exploit" in b:
            csv_files[f"canary_exploit_{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Language", "Challenge Type", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Score"
            ]
        elif "cyberseceval" in b:
            csv_files[f"instruct_and_autocomplete_{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Variant", "Language", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Bleu score", "Total count", "Vulnerable percentage",
                "Vulnerable suggestion count", "Pass rate"
            ]    
            csv_files[f"mitre_{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Category", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Refusal count", "Malicious count", "Benign count",
                "Total count", "Benign percentage", "Else count"
            ]
            csv_files[f"interpreter_{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Attack type", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Maliciousness Level",
                "Is extremely malicious",
                "Is potentially malicious",
                "Is non malicious",
                "Total count",
                "Malicious percentage"
            ]
            csv_files[f"frr_{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Language", "Attack type", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Judge Response",
                "Accept count",
                "Refusal count",
                "Refusal rate"
            ]
            csv_files[f"canary_exploit_{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Language", "Challenge Type", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Score"
            ]
        elif "mbpp" in b:
            csv_files[f"mbpp_{shot_prompting}_shot"] = [
                "LLM", "Benchmark prompt", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "MBPP pass@1 (unsanitized)", "MBPP+ pass@1 (unsanitized)", "GoogleBLEU (unsanitized)", "CodeBLEU (unsanitized)", "SacreBLEU (unsanitized)",
                "MBPP pass@1 (sanitized)", "MBPP+ pass@1 (sanitized)", "GoogleBLEU (sanitized)", "CodeBLEU (sanitized)", "SacreBLEU (sanitized)"
            ]            
        elif "all" in b:
            csv_files[f"humaneval_x_{shot_prompting}_shot"] = [
                "LLM", "Benchmark prompt", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Pass@1", "googleBLEU", "codeBLEU", "sacreBLEU"
            ]
            csv_files[f"instruct_and_autocomplete_{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Variant", "Language", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Bleu score", "Total count", "Vulnerable percentage",
                "Vulnerable suggestion count", "Pass rate"
            ]      
            csv_files[f"mitre_{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Category", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Refusal count", "Malicious count", "Benign count",
                "Total count", "Benign percentage", "Else count"
            ]        
            csv_files[f"interpreter_{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Attack type", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Maliciousness Level",
                "Is extremely malicious",
                "Is potentially malicious",
                "Is non malicious",
                "Total count",
                "Malicious percentage"
            ]
            csv_files[f"frr_{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Language", "Attack type", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Judge Response",
                "Accept count",
                "Refusal count",
                "Refusal rate"
            ]
            csv_files[f"canary_exploit_{shot_prompting}_shot"] = [
                "LLM", "Prompt ID", "Language", "Challenge Type", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "Score"
            ]
            csv_files[f"mbpp_{shot_prompting}_shot"] = [
                "LLM", "Benchmark prompt", "Execution time (s)", "CPU Energy (J)",
                "RAM Energy (J)", "GPU Energy (J)", "CPU Power (W)", "RAM Power (W)",
                "GPU Power (W)", "CO2 emissions (Kg)", "CO2 emissions rate (Kg/s)",
                "MBPP pass@1 (unsanitized)", "MBPP+ pass@1 (unsanitized)", "GoogleBLEU (unsanitized)", "CodeBLEU (unsanitized)", "SacreBLEU (unsanitized)",
                "MBPP pass@1 (sanitized)", "MBPP+ pass@1 (sanitized)", "GoogleBLEU (sanitized)", "CodeBLEU (sanitized)", "SacreBLEU (sanitized)"
            ]   
    return csv_files