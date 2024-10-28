    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= special_factorial(i)

    return result

