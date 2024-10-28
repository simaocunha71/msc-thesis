def max_run_uppercase(s):
    count = 0
    max_count = 0
    for i in s:
        if i.isupper():
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count