def max_run_uppercase(s: str) -> int:
    max_run = 0
    run = 0
    for i in range(len(s)):
        if s[i].isupper():
            run += 1
        else:
            run = 0
        max_run = max(max_run, run)
    return max_run