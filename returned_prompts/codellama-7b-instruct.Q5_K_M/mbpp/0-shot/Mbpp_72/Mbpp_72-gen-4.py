def dif_Square(n):
    return any(x**2 + y**2 == n for x in range(0, int(n**0.5)) for y in range(0, int(n**0.5)))
