    result = 1
    for i in range(n, 0, -1):
        result *= i * special_factorial(i - 1)
    return result


