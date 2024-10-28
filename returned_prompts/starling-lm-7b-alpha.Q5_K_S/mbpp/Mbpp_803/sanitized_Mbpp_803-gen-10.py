import math
def is_perfect_square(num):
    if num < 0:
        return False
    sqrt = math.sqrt(num)
    return int(sqrt) ** 2 == num