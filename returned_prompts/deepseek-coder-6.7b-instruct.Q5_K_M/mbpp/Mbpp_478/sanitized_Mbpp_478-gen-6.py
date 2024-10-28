def remove_lowercase(s):
    lower = 0
    upper = 0
    for i in s:
        if i.isupper():
            upper += 1
        else:
            if upper > lower:
                s = s.replace(s[lower:upper], '')
            lower = upper = 0
    if upper > lower:
        s = s.replace(s[lower:upper], '')
    return s