def max_product_tuple(tuples):
    max_product = 0
    for pair in tuples:
        product = abs(pair[0] * pair[1])
        if product > max_product:
            max_product = product
    return max_product