
import math
def dif_Square(n):
    for i in range(0, int(math.sqrt(n)) + 1):
        j = int(math.sqrt(n - i * i))
        if (i * i + j * j) == n:
            return True
    return False


