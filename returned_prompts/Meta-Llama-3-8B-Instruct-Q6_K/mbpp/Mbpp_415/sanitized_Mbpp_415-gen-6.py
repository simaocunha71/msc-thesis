from itertools import combinations
def max_Product(arr):
    max_product = 0
    pair = ()
    for p in combinations(arr, 2):
        product = p[0]*p[1]
        if product > max_product:
            max_product = product
            pair = p
    return pair