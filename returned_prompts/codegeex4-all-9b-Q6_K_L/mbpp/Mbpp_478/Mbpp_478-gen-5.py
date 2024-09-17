def remove_lowercase(s):
    res = ''
    for c in s:
        if c.isupper():
            res += c
    return res

