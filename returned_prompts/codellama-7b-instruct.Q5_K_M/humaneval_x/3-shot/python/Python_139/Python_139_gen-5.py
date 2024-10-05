    result = 1
    if n < 0:
        return result

    for i in range(n, 0, -1):
        result *= i

    return result


