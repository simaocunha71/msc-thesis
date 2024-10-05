    result = ''
    while x > 0:
        result = str(x % base) + result
        x = x // base

    return result

