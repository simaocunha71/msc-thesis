    result = []

    for c in string:
        if c.islower():
            result.append(c.upper())
        else:
            result.append(c.lower())

    return ''.join(result)


