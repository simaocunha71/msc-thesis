    result = ""
    while x > 0:
        result += str(x % base)
        x //= base
    return result[::-1]


