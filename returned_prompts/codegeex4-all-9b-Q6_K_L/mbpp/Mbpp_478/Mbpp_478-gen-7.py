def remove_lowercase(s):
    s = list(s)
    for i in range(len(s)):
        if s[i].islower():
            s[i] = ""
    return "".join(s)

