
def max_product_tuple(tuples):
    max_product = -float('inf')
    for tup1, tup2 in zip(tuples, tuples[1:] + [(0, 0)]):
        prod1 = tup1[0] * tup2[0]
        prod2 = tup1[1] * tup2[1]
        prod3 = tup1[0] * tup2[1]
        prod4 = tup1[1] * tup2[0]
        max_product = max(max_product, abs(prod1), abs(prod2), abs(prod3), abs(prod4))
    return max_product


