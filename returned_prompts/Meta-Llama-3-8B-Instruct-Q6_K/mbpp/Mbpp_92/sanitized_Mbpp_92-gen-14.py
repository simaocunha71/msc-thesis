def is_undulating(n):
    s = str(n)
    for i in range(1, len(s)):
        if (s[i-1] == s[i]):
            return False
    return True