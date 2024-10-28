    s = str(x)
    n = len(s)
    if shift > n:
        return s[::-1]
    return s[n-shift:] + s[:n-shift]


