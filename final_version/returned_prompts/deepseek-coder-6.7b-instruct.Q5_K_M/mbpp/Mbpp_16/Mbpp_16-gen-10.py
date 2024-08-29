def text_lowercase_underscore(s):
    return any(x.islower() and y.islower() and z.islower() for x, y, z in zip(s, s[1:], s[2:]))

print(text_lowercase_underscore("aab_cbbbc"))

