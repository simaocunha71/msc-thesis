def max_run_uppercase(s):
    n = len(s)
    if n == 0:
        return 0
    i, j = 0, 0
    max_run = 0
    while j < n:
        if s[j].isupper():
            if i == j:
                i += 1
            j += 1
        else:
            max_run = max(max_run, j - i)
            i = j
            j += 1
    max_run = max(max_run, j - i)
    return max_run