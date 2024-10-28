def text_lowercase_underscore(text):
    return any(c.islower() for c in text) and "_" in text