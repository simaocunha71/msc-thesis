def max_product_tuple(tuples):
    return max(map(lambda x: abs(x[0]) * abs(x[1]), tuples))


