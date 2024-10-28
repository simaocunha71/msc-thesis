    result = [n]
    n = n + 1 if n % 2 == 0 else n + 2

    while n != 1:
        n = n + 1 if n % 2 == 0 else n + 2
        result.append(n)

    return result


