"""
def max_run_uppercase(s):
    curr = 0
    max_run = 0
    for c in s:
        if c.isupper():
            curr += 1
            if curr > max_run:
                max_run = curr
        else:
            curr = 0
    return max_run
"""
