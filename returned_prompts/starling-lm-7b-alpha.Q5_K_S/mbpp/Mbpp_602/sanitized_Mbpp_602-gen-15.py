def first_repeated_char(s):
    d = {}
    for i in s:
        if i in d:
            return i
        d[i] = 1
    return None