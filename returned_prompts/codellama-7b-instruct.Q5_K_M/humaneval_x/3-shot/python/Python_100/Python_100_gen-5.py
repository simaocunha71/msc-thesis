    result = []

    while n:
        result.append(n)
        n = (n + 1) if n % 2 else n + 2

    return result[::-1]


