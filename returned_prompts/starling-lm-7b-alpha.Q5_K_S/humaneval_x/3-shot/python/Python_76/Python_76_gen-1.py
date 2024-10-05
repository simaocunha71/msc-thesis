    while x > 1:
        if x % n != 0:
            return False
        x = x // n
    return x == 1


