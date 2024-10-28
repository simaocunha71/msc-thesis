def max_run_uppercase(s):
    max_count = 0
    current_count = 0
    for c in s:
        if c.isupper():
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count