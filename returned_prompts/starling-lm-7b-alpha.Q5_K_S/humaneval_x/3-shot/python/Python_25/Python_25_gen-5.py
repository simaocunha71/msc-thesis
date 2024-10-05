    result = []
    factor = 2
    while n > 1 and factor * factor <= n:
        while n % factor == 0:
            result.append(factor)
            n = n / factor
        factor += 1

    if n > 1:
        result.append(n)

    return result


