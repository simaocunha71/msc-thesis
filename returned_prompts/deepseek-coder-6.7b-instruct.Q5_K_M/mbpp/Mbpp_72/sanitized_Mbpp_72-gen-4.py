def dif_Square(n):
    j = 0
    while j*j <= n:
        i = 0
        while i*i <= n:
            if i*i + j*j == n:
                return True
            i += 1
        j += 1
    return False