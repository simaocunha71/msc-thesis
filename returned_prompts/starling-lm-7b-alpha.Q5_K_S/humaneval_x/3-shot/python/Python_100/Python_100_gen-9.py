    result = []
    n = float(n)
    while n > 0:
        if n % 2 == 0:
            result.append(int(n))
            n = n + 1
        else:
            result.append(int(n))
            n = n + 2
    return result


