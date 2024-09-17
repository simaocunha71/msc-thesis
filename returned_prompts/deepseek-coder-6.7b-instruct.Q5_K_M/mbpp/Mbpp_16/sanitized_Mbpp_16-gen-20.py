def text_lowercase_underscore(s):
    return all(x.islower() or x=='_' for x in s.split('_'))