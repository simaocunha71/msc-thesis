def dif_Square(n):
    for i in range(1, int(n**0.5) + 1):
        if (i**2 - (n - i**2) ** 0.5 ** 2) == int((n - i**2) ** 0.5) ** 2:
            return True
    return False