def dif_Square(n):
    for i in range(1,int(n**0.5)+1):
        if i*i - n in range(1,n):
            return True
    return False