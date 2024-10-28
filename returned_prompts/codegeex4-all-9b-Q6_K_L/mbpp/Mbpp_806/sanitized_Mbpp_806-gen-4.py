def max_run_uppercase(s):
    max_length = 0
    current_length = 0
    for c in s:
        if c.isupper():
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    return max_length