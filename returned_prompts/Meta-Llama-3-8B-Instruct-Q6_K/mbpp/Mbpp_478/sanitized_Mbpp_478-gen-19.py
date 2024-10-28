def remove_lowercase(s):
    result = ''
    for c in s:
        if c.isupper():
            result += c
    return result