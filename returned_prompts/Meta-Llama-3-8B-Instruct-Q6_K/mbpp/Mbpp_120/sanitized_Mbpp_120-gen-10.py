def max_product_tuple(tup_list):
    max_product = 0
    for tup in tup_list:
        product = tup[0] * tup[1]
        if product > max_product:
            max_product = product
    return max_product