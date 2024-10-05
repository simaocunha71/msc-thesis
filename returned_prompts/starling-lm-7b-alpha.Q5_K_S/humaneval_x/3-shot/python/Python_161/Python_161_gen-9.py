    result = []
    for c in s:
        if c.isalpha():
            result.append(c.swapcase())
        else:
            result.append(c)
    return ''.join(result)


