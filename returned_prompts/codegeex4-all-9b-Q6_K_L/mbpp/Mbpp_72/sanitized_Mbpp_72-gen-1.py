def dif_Square(n):
    for i in range(1, int(n**0.5) + 1):
        if (n + i) ** 0.5 == int((n + i) ** 0.5) and (n - i) ** 0.5 == int((n - i) ** 0.5):
            return True
    return False