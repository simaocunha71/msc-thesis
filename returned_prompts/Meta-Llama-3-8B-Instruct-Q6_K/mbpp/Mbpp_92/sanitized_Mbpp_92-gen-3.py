def is_undulating(n):
    s = str(n)
    return s == s[0] * len(s) or s == s[0] + s[-1] * (len(s) - 2) + s[0] or s == s[0] + s[-1] * (len(s) - 1) + s[0]