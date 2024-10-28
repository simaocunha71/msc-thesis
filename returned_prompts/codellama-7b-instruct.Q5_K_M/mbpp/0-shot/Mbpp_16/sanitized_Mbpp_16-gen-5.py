def text_lowercase_underscore(s):
    s = s.lower()
    for i in range(len(s)-1):
        if s[i]=='_' and s[i+1].islower():
            continue
        else:
            return False
    return True