    sum_product_tuple = (0, 1)
    for elem in numbers:
        sum_product_tuple = (sum_product_tuple[0] + elem, sum_product_tuple[1] * elem)
    return sum_product_tuple


