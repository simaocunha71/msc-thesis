def remove_lowercase(s):
    for c in s:
        if c.islower():
            s = s.replace(c, '')
    return s