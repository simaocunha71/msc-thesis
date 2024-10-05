    if n == 0:
        return 0
    elif n == 1:
        return 2
    else:
        return (2 ** (n - 1)) + (2 ** (n - 2))


