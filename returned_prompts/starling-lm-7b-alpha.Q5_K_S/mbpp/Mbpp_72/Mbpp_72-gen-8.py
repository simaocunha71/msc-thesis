
def dif_Square(n):
    for i in range(1, n):
        if i * i - n in range(1, n):
            return True
    return False


