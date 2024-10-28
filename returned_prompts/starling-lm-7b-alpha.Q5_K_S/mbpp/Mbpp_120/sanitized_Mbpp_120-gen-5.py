def max_product_tuple(tups):
    max_product = 0
    for tup in tups:
        product = tup[0] * tup[1]
        max_product = max(max_product, product)
    return max_product