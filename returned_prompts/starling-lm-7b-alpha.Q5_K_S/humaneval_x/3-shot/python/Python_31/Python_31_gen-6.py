    if n == 1 or n == 0:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(n ** 0.5) + 1

    for divisor in range(3, sqrt_n, 2):
        if n % divisor == 0:
            return False

    return True


