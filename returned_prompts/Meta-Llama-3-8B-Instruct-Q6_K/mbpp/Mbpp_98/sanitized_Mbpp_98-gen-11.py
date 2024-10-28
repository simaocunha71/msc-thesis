import math
def multiply_num(lst):
    result = 1
    for num in lst:
        result *= num
    return result / len(lst)