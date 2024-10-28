def text_lowercase_underscore(s):
    return all(c.islower() or c == '_' for c in s) and len(set(c for c in s if c != '_')) <= 26