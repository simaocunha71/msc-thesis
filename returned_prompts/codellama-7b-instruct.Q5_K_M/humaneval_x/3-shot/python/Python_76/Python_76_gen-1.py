    if x < 0 or n < 0:
        return False

    if x == 0 and n == 0:
        return False

    if x == 0 and n != 0:
        return True

    if int(x ** (1 / n)) ** n == x:
        return True
    else:
        return False


