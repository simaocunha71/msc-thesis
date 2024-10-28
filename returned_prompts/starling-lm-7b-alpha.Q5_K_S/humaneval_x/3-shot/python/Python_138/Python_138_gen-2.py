    if n % 2 != 0:
        return False
    if n < 8:
        return False
    return (n - 4) % 4 == 0


