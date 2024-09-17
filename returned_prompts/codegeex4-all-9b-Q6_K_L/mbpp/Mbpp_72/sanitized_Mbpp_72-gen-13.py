def dif_Square(n):
    for i in range(1,int(math.sqrt(n))+1):
        if n == i*i + i*i:
            return True
    return False