def remove_lowercase(s):
    if not s:
        return s
    for i in range(len(s)):
        if s[i].isupper():
            return s[:i] + remove_lowercase(s[i:])
    return s