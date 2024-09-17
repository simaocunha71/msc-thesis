def dif_Square(n):
    for i in range(1, n + 1):
        if i * i - n in range(1, n + 1):
            return True
    return False