def text_lowercase_underscore(s):
    return all(c.islower() for c in s) and s.replace('_', '').islower()


