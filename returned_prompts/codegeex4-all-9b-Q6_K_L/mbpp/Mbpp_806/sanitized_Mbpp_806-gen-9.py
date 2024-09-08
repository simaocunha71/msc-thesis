def max_run_uppercase(s):
    max_run = 0
    current_run = 0
    for c in s:
        if c.isupper():
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    return max_run