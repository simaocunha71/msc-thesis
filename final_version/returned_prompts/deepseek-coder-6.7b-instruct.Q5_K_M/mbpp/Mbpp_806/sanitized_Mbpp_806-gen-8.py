def max_run_uppercase(s):
    max_run = 0
    current_run = 0
    for c in s:
        if c.isupper():
            current_run += 1
        else:
            if current_run > max_run:
                max_run = current_run
            current_run = 0
    return max(max_run, current_run)