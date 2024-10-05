    if x == 1:
        return True
    while x > 1:
        x /= n
        if x == 1:
            return True
    return False

