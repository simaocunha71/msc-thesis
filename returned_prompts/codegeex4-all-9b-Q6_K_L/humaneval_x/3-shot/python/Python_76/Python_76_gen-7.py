    if x <= 1:
        return False

    for i in range(1, int(x ** 0.5) + 1):
        if x ** (1 / i) == n:
            return True

    return False


