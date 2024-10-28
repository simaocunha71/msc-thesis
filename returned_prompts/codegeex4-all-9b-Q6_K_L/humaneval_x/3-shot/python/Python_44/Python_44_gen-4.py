    result = []
    while x > 0:
        remainder = x % base
        result.append(str(remainder))
        x //= base

    return ''.join(result[::-1])


