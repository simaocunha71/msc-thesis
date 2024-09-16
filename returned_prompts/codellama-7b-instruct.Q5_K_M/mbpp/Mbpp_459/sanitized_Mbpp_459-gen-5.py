def remove_uppercase(s):
    t = ''
    for i in range(len(s)):
        if s[i].islower():
            t += s[i]
    return t