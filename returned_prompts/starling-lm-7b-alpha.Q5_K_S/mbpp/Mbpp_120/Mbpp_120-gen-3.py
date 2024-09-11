"""
def max_product_tuple(list_tuple):
    max_product = 0
    for i in range(len(list_tuple)):
        for j in range(i+1, len(list_tuple)):
            product = abs(list_tuple[i][0]*list_tuple[j][0])
            if product > max_product:
                max_product = product
    return max_product
"""

def max_product_tuple(list_tuple):
    max_product = 0
    for tuple1 in list_tuple:
        for tuple2 in list_tuple:
            product = abs(tuple1[0]*tuple2[0])
            if product > max_product:
                max_product = product
    return max_product

# test
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
assert max_product_tuple([(3, 5), (3, 7), (8, 2), (9, 1)]) == 45
assert max_product_tuple([(4, 10), (3, 9), (2, 8), (5, 7)]) == 80

# test edge cases
assert max_product_tuple([(0, 0), (0, 0), (0, 0), (0, 0)]) == 0
assert max_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1)]) == 1
assert max_product_tuple([(1, 1), (1, 1), (1, 1), (1, 1)]) == 1
assert max_product_tuple([(1000, 1000), (1000, 1000), (1000, 1000), (1000, 1000)]) == 1000000000

print("All tests passed.")





















"""
def max_