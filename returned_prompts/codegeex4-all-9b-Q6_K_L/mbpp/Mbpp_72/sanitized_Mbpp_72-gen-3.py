def dif_Square(n):
    for i in range(1, int(n**0.5)+1):
        if n == i*i + (n-i*i):
            return True
    return False