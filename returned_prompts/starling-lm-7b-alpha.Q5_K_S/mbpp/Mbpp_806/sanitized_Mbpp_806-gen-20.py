def max_run_uppercase(s):
    if not s:
        return 0
    i = 0
    j = 0
    while i < len(s):
        if s[i].isupper():
            j = i
            while j < len(s) and s[j].isupper():
                j += 1
            break
        i += 1
    return j - i + 1