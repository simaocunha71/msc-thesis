def dif_Square(n):
    for i in range(1, int(n**0.5) + 1):
        for j in range(i, int(n**0.5) + 1):
            if i**2 - j**2 == n:
                return True
    return False