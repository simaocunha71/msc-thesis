def dif_Square(n):
    for i in range(1, int(math.sqrt(n))+1):
        if math.sqrt(n + i*i).is_integer():
            return True
    return False