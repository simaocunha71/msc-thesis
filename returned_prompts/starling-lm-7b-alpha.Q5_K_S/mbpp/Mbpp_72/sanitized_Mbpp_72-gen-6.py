import math
def dif_Square(num):
    sqrt_num = int(math.sqrt(num))
    for i in range(sqrt_num, 0, -1):
        if (i * i - num) == 0:
            return True
    return False