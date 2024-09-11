def text_lowercase_underscore(s):
    s = s.lower()
    for i in range(len(s)-1):
        if s[i].isalpha() and s[i+1].isalpha() and s[i+1] != '_':
            return False
    return True