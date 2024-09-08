def is_undulating(n):
    s = str(n)
    if len(s) < 3:
        return False
    for i in range(1, len(s) - 1):
        if s[i] == s[i - 1] or s[i] == s[i + 1]:
            return False
    return True