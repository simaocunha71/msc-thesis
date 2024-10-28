def dif_Square(n):
    a = 0
    while a * a <= n:
        b = int(math.sqrt(n - a * a))
        if a * a + b * b == n:
            return True
        a += 1
    return False