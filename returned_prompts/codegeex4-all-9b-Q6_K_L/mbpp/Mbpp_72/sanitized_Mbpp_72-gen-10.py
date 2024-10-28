def dif_Square(n):
    i = 1
    while i*i <= n:
        j = int(i*i)
        if n == j*(j+2*i) or n == j*(j-2*i):
            return True
        i += 1
    return False