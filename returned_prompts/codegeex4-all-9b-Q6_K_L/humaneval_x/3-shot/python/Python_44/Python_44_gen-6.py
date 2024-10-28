    if base >= 10 or base <= 1:
        return None

    result = []
    while x > 0:
        result.append(str(x % base))
        x = x // base

    return ''.join(result[::-1])


