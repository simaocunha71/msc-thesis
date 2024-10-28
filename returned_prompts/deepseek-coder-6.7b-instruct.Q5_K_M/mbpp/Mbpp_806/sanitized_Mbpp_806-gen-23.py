def max_run_uppercase(s):
    max_count = 0
    count = 0
    for i in s:
        if i.isupper():
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count