
def dif_Square(n):
    for i in range(1, int(n ** 0.5) + 1):
        j = int(n - i ** 2)
        if j == 1:
            return True
        if j == 0:
            return False
    return False


