    if x < 1:
        return False

    while x % n == 0:
        x /= n

    return x == 1

