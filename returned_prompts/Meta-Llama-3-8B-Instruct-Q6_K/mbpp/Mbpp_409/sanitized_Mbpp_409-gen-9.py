def min_product_tuple(tuples):
    min_product = float('inf')
    for pair in tuples:
        product = pair[0] * pair[1]
        if product < min_product:
            min_product = product
    return min_product