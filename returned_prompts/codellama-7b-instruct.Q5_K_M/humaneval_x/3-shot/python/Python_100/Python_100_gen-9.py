    result = []
    while n > 0:
        result.append(n)
        n = (n + 1) // 2

    return result[::-1]


