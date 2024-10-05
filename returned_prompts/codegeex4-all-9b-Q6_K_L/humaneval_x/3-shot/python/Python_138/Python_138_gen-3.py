    if n % 2 != 0:
        return False

    for i in range(2, n, 2):
        if n - i >= 0 and (n - i) % 2 == 0:
            return True

    return False

