    if n == 1:
        return x > 0
    while x > 1:
        x /= n
    return x == 1


