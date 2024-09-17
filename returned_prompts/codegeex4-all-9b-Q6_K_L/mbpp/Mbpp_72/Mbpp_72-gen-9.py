def dif_Square(n):
    for i in range(1, int(math.sqrt(n))+1):
        j = math.sqrt(n - i*i)
        if j == int(j):
            return True
    return False