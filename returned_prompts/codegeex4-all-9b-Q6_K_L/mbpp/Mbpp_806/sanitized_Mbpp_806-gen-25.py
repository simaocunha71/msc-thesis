def max_run_uppercase(s: str) -> int:
    run_length = 0
    max_run_length = 0
    for char in s:
        if char.isupper():
            run_length += 1
            if run_length > max_run_length:
                max_run_length = run_length
        else:
            run_length = 0
    return max_run_length