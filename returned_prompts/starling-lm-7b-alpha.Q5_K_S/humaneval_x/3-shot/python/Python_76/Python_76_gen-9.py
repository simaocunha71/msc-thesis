    while x % n == 0:
        x = x // n
        if x == 1:
            return True
    return False


