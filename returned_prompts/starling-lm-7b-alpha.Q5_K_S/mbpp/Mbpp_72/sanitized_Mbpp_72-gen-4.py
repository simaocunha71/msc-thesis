from math import sqrt
def dif_Square(n):
    for i in range(int(n**0.5), -1, -1):
        if n % i == 0:
            return True
    return False