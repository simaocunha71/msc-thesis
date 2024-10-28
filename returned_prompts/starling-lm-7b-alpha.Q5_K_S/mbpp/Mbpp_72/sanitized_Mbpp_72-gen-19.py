def dif_Square(n):
    for i in range(1, n):
        if i * i > n:
            break
        if (i * i - n) % (2 * i) == 0:
            return True
    return False