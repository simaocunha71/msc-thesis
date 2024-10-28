    if a == 0:
        return True

    for i in range(-10000, 10000):
        if i ** 3 == a:
            return True

    return False

