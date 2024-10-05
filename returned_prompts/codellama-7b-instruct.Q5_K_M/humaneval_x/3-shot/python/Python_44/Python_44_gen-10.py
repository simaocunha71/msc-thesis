    result = ''

    while x:
        result = str(x % base) + result
        x //= base

    return result


