    result = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            result.append(d)
            n = n // d
        d += 1
    if n > 1:
        result.append(n)
    return result


