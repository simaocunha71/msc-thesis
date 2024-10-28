    result = []
    n = int(n)
    while n > 0:
        if n % 2 == 0:
            result.append(n)
            n -= 2
        else:
            result.append(n)
            n += 1
    return result


