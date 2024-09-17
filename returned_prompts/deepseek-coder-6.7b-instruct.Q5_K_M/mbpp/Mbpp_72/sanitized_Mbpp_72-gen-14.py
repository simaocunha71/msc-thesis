import math
def dif_Square(n):
    for i in range(0, int(math.sqrt(n)) + 1):
        j = 0
        while ((i * i) + (j * j) <= n):
            if ((i * i) + (j * j) == n):
                return True
            j += 1
    return False