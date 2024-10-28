    result = ''
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base

    return result

