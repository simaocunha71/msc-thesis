def max_product_tuple(lst):
    max_product = float('-inf')
    for tup in lst:
        product = abs(tup[0] * tup[1])
        if product > max_product:
            max_product = product
    return max_product