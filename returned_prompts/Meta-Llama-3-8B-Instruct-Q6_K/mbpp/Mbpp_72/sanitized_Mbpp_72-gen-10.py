def dif_Square(n):
    a = 0
    while a**2 <= n:
        b = int((n - a**2)**0.5)
        if a**2 + b**2 == n:
            return True
        a += 1
    return False