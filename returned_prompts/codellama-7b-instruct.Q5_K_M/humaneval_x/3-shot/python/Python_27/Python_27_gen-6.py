    result = []
    for c in string:
        if c.islower():
            result.append(c.upper())
        elif c.isupper():
            result.append(c.lower())
        else:
            result.append(c)

    return ''.join(result)


