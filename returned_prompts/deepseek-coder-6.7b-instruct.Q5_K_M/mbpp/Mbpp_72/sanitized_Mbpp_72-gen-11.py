def dif_Square(n):
    for i in range(0, n + 1):
        j = 0
        while i * i + j * j <= n * n:
            if i * i + j * j == n * n:
                return True
            j += 1
    return False