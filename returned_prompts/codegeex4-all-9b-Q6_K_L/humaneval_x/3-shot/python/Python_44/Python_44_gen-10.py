    result = []
    while x > 0:
        result.insert(0, str(x % base))
        x //= base

    return ''.join(result)

