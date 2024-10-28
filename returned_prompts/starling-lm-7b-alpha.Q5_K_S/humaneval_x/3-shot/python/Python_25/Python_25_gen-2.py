    result = []
    d = 2
    while n > 1:
        while n % d != 0:
            d += 1
        result.append(d)
        n //= d
    return result


