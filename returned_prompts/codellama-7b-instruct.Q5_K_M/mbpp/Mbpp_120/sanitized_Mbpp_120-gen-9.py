def max_product_tuple(list_of_tuple):
    return max(map(lambda x: x[0] * x[1], list_of_tuple))