    result = []
    while x:
        result.append(str(x % base))
        x //= base
    return "".join(result[::-1])


