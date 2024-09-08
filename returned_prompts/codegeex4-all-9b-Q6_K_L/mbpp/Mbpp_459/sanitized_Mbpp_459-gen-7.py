def remove_uppercase(s):
    result = ''
    i = 0
    while i < len(s):
        if s[i].isupper():
            i += 1
            while i < len(s) and s[i].islower():
                result += s[i]
                i += 1
        else:
            result += s[i]
            i += 1
    return result