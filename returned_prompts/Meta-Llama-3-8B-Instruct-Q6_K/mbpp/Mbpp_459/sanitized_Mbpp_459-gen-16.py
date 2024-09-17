def remove_uppercase(s):
    result = ''
    for i, c in enumerate(s):
        if c.islower():
            result += c
        elif i > 0 and s[i-1].islower():
            result += c
    return result