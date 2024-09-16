def is_undulating(n):
    s = str(n)
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            return True
    return False
