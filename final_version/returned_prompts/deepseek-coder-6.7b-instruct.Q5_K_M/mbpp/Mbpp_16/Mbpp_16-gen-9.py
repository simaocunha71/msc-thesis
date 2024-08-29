def text_lowercase_underscore(s):
    return all(c.islower() or c == "_" for c in s)

print(text_lowercase_underscore("aab_cbbbc")) # True

