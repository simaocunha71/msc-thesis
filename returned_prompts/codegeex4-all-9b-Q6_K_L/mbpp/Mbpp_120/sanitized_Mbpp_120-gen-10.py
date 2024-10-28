def max_product_tuple(tuples):
    max_product = 0
    for t in tuples:
        product = abs(t[0] * t[1])
        if product > max_product:
            max_product = product
    return max_product