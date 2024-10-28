
def max_run_uppercase(s):
    count = max_count = 0
    for char in s:
        if char.isupper():
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count


