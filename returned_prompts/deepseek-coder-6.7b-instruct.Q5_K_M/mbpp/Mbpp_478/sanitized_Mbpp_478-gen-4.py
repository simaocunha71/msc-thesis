def remove_lowercase(s):
    res = ""
    for i in range(len(s)):
        if s[i].isupper():
            res += s[i]
    return res