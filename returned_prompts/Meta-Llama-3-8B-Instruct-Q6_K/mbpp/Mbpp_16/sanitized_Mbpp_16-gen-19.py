def text_lowercase_underscore(s):
    if not s:
        return False
    for i in range(len(s)):
        if i > 0 and s[i].isupper():
            return False
        if i > 0 and s[i-1] == '_':
            if not s[i].islower():
                return False
    return True