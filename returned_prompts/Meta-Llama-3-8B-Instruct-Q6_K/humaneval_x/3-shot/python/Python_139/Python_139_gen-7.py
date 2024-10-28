    result = 1
    for i in range(1, n+1):
        result *= i
    for i in range(n, 1, -1):
        result *= i
    return result


