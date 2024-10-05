    if n == 1 and x > 0:
        return True
    while x > 1:
        x = x / n
        if x == 1:
            return True
    return False


