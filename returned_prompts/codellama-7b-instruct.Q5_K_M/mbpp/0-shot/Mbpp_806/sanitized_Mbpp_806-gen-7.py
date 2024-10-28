def max_run_uppercase(s):
    max_run = 0
    run = 0
    for c in s:
        if c.isupper():
            run += 1
        else:
            if run > max_run:
                max_run = run
            run = 0
    return max(max_run, run)