    result = []
    for d in range(2, n + 1):
        while n % d == 0:
            result.append(d)
            n //= d
    return result


