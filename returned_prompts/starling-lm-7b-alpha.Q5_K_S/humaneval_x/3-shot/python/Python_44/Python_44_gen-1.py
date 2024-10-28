    if x == 0:
        return '0'

    result = []
    while x > 0:
        result.append(str(x % base))
        x //= base

    return ''.join(result[::-1])


