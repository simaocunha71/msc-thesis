import math
def multiply_num(lst):
    product = 1
    for num in lst:
        product *= num
    return product / len(lst) if len(lst) > 0 else 0