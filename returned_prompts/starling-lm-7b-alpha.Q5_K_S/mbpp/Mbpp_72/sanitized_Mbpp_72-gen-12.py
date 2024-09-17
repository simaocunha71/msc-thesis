def dif_Square(n):
    i = 0
    while i*i < n:
        if (n - i*i)**0.5 == int((n - i*i)**0.5):
            return True
        i += 1
    return False