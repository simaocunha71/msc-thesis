def multiply_num(lst):
    product = 1
    for num in lst:
        product *= num
    return product / len(lst)

assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""

