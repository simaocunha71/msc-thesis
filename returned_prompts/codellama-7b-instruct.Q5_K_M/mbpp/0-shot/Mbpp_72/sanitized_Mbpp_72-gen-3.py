def dif_Square(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i**2 + j**2 == n**2:
                return True
    return False