def max_product_tuple(tuple_list):
    max_product = 0
    for pair in tuple_list:
        product = pair[0] * pair[1]
        if product > max_product:
            max_product = product
    return max_product