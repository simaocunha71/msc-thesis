def dif_Square(n):
    if n < 0:
        return False
    for i in range(1, int(n**0.5) + 1):
        if (i * i - (n - i * i)) % 2 == 0:
            return True
    return False