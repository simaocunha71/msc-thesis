def text_lowercase_underscore(s):
    return all(c.islower() or c == '_' for c in s.replace("_", "")) and s.replace("_", "").isalpha() and s.count("_") > 0