    digits = '0123456789ABCDEF'
    result = ''

    while x > 0:
        result = digits[x % base] + result
        x //= base

    return result


