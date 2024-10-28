def dif_Square(n):
    if n < 0:
        return False
    for i in range(int((n + 1) ** 0.5)):
        if (i * i - (n - i * i)) % 4 == 1:
            return True
    return False