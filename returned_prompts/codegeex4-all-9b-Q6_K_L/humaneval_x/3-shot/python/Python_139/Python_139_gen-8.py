    if n == 0:
        return 1

    result = 1
    for i in range(n, 0, -1):
        result *= i

    return result

