    result = []

    for c in string:
        if c.isupper():
            result.append(c.lower())
        else:
            result.append(c.upper())

    return ''.join(result)

