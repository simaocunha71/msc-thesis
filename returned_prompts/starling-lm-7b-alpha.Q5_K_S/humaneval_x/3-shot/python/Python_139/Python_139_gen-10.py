    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return n * special_factorial(n - 1)


