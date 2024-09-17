def snake_to_camel(s):
    result = ''
    for i, c in enumerate(s):
        if c == '_':
            result += c[1].upper()
        else:
            result += c
    return result