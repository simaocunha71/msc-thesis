def max_run_uppercase(s):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count, max_count = 0, 0
    for char in s:
        if char in upper:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count