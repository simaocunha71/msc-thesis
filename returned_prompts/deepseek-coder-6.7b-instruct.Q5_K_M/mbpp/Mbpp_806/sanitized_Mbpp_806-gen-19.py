def max_run_uppercase(s):
    max_count, count = 0, 0
    for ch in s:
        if ch.isupper():
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count