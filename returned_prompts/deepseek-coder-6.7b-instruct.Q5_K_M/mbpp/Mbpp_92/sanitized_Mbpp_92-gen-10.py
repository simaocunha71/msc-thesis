def is_undulating(n):
    s = str(n)
    prev = None
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] or (prev is not None and prev == s[i]):
            return False
        prev = s[i]
    return True