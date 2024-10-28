def max_run_uppercase(s):
    """Return the maximum run of uppercase characters in the given string."""
    max_run = 0
    run = 0
    for c in s:
        if c.isupper():
            run += 1
            if run > max_run:
                max_run = run
        else:
            run = 0
    return max_run
