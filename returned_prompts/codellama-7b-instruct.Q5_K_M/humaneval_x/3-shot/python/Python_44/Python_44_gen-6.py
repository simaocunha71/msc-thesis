    digits = ['0', '1', '2', '3', '4', '5', '6', '7']
    if x == 0:
        return '0'

    result = ''
    while x > 0:
        result = digits[x % base] + result
        x //= base

    return result


