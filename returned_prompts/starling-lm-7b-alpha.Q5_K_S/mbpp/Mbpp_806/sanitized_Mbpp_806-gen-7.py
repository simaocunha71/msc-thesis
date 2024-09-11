def max_run_uppercase(s):
    prev = s[0].isupper()
    run_length = 0
    max_run = 0
    for c in s:
        if c.isupper() == prev:
            run_length += 1
        else:
            max_run = max(max_run, run_length)
            run_length = 1
        prev = c.isupper()
    max_run = max(max_run, run_length)
    return max_run