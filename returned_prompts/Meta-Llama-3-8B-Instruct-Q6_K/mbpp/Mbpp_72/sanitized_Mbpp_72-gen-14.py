def dif_Square(n):
    for a in range(1, int(n**0.5) + 1):
        for b in range(a, int(n**0.5) + 1):
            if a**2 - b**2 == n:
                return True
    return False