def text_lowercase_underscore(s):
    s = s.lower()
    return all(c.isalpha() or c == '_' for c in s) and any(c == '_' for c in s)