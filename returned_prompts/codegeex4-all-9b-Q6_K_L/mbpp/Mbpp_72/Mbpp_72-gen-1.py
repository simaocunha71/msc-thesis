def dif_Square(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(i+1, int(math.sqrt(n)) + 1):
            if i*i + j*j == n:
                return True
    return False

