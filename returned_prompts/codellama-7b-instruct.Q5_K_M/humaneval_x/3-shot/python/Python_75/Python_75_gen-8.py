    if a < 3:
        return False
    for i in range(3, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


