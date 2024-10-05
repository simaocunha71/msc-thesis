    if x <= 1:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x**i == x:
            return True

    return False

