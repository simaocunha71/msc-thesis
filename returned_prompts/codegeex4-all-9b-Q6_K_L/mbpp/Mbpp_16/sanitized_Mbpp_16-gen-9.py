def text_lowercase_underscore(s):
    for c in s:
        if not c.islower() and c != '_':
            return False
    return True