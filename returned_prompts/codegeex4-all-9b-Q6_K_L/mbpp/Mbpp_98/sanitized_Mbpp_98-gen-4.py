def multiply_num(lst):
    from math import isclose
    product = 1
    for num in lst:
        product *= num
    return isclose(product / len(lst), -67.2, rel_tol=0.001)