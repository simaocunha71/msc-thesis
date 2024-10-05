    if n < 4:
        return False
    if n % 2 == 1:
        return False

    for i in range(0, n, 2):
        if i + 2 + i + 4 + i + 6 + i + 8 == n:
            return True

    return False


