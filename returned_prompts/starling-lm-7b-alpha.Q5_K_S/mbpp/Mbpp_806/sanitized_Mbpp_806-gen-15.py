def max_run_uppercase(s):
    r = 0
    c = 0
    for i in range(len(s)):
        if s[i].isupper():
            c += 1
        else:
            c = 0
        r = max(r, c)
    return r