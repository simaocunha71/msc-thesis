    if n < 4:
        return False
    if n % 2 != 0:
        return False
    if n == 4:
        return False
    if n == 6:
        return False
    if n == 8:
        return True
    if n == 10:
        return True
    if n == 12:
        return True
    if n == 14:
        return True
    if n > 14:
        return False


