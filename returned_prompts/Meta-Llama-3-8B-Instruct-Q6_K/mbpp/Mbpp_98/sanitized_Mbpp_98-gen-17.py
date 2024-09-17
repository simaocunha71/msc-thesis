import math
def multiply_num(lst):
    total = 1
    for num in lst:
        total *= num
    return total / len(lst)