    if x == 1:
        return True
    if x < 1 or n < 1:
        return False

    while x > 1:
        x = x / n
        if x == 1:
            return True

    return False


