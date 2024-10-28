    result = []

    for c in s:
        if c.isalpha():
            if c.islower():
                result.append(c.upper())
            else:
                result.append(c.lower())
        else:
            result.append(c)

    if not any(c.isalpha() for c in s):
        result.reverse()

    return ''.join(result)

