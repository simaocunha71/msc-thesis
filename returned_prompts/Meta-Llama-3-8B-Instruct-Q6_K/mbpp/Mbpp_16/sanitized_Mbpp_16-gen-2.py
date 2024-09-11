def text_lowercase_underscore(s):
    if not s:
        return False
    if s[0].islower():
        for char in s[1:]:
            if not char.islower() and char != '_':
                return False
    else:
        return False
    return True