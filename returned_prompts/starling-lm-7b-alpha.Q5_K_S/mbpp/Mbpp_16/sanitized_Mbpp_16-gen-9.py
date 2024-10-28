def text_lowercase_underscore(s):
    return any(s.find(c) != -1 for c in "_abcdefghijklmnopqrstuvwxyz")