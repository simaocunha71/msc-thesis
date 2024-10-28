def max_product_tuple(list_tuple):
    max_product = 0
    for tuple1 in list_tuple:
        for tuple2 in list_tuple:
            product = abs(tuple1[0]*tuple2[0])
            if product > max_product:
                max_product = product
    return max_product