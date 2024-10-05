    if base < 2 or base > 9:
        return 'Invalid base'

    digits = '0123456789'
    result = ''

    while x > 0:
        result = digits[x % base] + result
        x //= base

    return result


