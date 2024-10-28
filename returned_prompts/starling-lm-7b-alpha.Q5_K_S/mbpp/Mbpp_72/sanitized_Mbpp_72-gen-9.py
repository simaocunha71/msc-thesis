def dif_Square(n):
    for i in range(1,n+1):
        if i*i - (n-i) == n:
            return True
    return False