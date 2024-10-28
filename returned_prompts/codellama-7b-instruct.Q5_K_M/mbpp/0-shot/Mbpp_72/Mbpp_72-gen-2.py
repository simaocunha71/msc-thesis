def dif_Square(n):
    for i in range(1, int(n ** 0.5) + 1):
        j = n - i ** 2
        if j < i ** 2:
            break
        if j == 0:
            return True
    return False
