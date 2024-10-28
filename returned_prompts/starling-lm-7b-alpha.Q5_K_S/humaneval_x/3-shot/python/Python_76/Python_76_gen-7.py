    while x % n == 0:
        if x == 1:
            return True
        x //= n
    return False


