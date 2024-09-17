def dif_Square(n):
    for i in range(1, int(n**0.5)):
        j = int(n - i**2)
        if j == i**2:
            return True
    return False