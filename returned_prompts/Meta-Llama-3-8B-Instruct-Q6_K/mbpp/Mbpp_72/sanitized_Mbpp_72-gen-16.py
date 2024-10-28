def dif_Square(n):
    for i in range(n + 1):
        for j in range(i + 1):
            if i * i - j * j == n:
                return True
    return False