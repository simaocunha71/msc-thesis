def is_polite(n):
    if n < 10:
        return n
    s = str(n)
    if (s[0] - '0') == 1 and (s[1] - '0') == 1:
        return n + 11
    elif (s[1] - '0') == 1 and (s[2] - '0') == 1:
        return n + 10
    else:
        return n + 1