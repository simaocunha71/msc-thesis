def max_product_tuple(num_pairs: list) -> int:
    return max(map(lambda x: x[0]*x[1], num_pairs))