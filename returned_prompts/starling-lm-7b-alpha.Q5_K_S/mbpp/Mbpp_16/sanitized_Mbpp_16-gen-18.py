def text_lowercase_underscore(s):
    return any(i.isalpha() for i in s) and not any(i.isupper() for i in s)