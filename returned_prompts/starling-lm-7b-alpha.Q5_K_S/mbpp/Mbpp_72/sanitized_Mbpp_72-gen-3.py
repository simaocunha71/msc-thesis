def dif_Square(n):
    for i in range(1,n):
        if i**2 - (n-i)**2 == n:
            return True
    return False