def text_lowercase_underscore(s):
    return all(c.islower() or c == '_' for c in s) and s.replace("_", "").isalpha()