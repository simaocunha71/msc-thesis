import math
def is_perfect_square(n):
    if n < 0:
        return False
    sqrt = math.sqrt(n)
    return sqrt*sqrt == n