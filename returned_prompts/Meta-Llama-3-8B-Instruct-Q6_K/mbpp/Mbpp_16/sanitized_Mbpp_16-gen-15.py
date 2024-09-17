def text_lowercase_underscore(s):
    for i in range(1, len(s)):
        if s[i].islower() and s[i-1].islower() and s[i-1] != '_':
            return False
        if s[i] == '_' and not s[i-1].islower():
            return False
    return True