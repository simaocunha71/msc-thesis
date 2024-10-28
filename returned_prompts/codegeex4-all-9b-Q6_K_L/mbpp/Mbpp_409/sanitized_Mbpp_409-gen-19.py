def min_product_tuple(tuples: list) -> int:
    return min(tuples, key=lambda x: x[0]*x[1])[0]*min(tuples, key=lambda x: x[0]*x[1])[1]