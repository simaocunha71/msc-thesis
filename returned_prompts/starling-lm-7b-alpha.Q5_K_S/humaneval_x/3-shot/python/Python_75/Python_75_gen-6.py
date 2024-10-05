    if a % 2 == 0:
        return False

    for i in range(3, int(a ** 0.5) + 1, 2):
        if a % i == 0:
            return False

    return True


