    result = []

    while n != 0:
        result.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n // 2) + 1

    return result[::-1]


