def dif_Square(n):
    i = 0
    while i * i <= n:
        j = 0
        while j * j <= n:
            if i * i + j * j == n:
                return True
            j += 1
        i += 1
    return False