import math
def next_Perfect_Square(n):
    sqrt_n = int(math.sqrt(n))
    sqrt_n += 1
    while math.ceil(math.sqrt(sqrt_n ** 2)) != sqrt_n:
        sqrt_n += 1
    return sqrt_n ** 2