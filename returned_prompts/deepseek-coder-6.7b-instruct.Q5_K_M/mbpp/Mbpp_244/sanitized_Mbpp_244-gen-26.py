import math
def next_Perfect_Square(num):
    sqrt_num = math.sqrt(num)
    if sqrt_num.is_integer():
        return (sqrt_num+1)**2
    else:
        return "No perfect square found"