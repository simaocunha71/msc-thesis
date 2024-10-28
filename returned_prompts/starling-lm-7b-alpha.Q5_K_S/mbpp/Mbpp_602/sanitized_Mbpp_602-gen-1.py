def first_repeated_char(s):
    d = {}
    for c in s:
        if c in d:
            return c
        d[c] = 1
    return "No repeated character"