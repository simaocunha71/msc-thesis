def toggle_string(s):
    res = ''
    for c in s:
        if c.islower():
            res += c.upper()
        elif c.isupper():
            res += c.lower()
        else:
            res += c
    return res