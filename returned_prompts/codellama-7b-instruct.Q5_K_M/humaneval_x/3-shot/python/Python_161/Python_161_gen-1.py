    result = []
    for c in s:
        if c.isalpha():
            result.append(c.upper() if c.islower() else c.lower())
        else:
            result.append(c)

    return ''.join(result)
