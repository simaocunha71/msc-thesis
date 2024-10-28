    result = []
    while n:
        result.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n + 1) // 2

    return result


