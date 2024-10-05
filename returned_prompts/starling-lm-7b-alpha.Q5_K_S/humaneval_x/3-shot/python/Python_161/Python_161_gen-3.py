    result = []
    for c in s:
        if c.isalpha():
            result.append(c.lower() if c.isupper() else c.upper())
        else:
            result.append(c)

    return ''.join(result) if result else s


