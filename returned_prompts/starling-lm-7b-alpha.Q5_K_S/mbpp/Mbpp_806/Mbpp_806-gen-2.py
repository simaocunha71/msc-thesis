"""
def max_run_uppercase(s):
    count = 0
    max_count = 0
    for c in s:
        if c.isupper():
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count
"""

