def dif_Square(n):
    for i in range(0, int(n ** 0.5)):
        for j in range(0, int(n ** 0.5)):
            if (i ** 2) + (j ** 2) == n:
                return True
    return False
