def max_product_tuple(tuple_list: list) -> int:
    max_product = 0
    for tup1, tup2 in zip(tuple_list, tuple_list[1:]):
        max_product = max(max_product, abs(tup1[0] * tup1[1] - tup2[0] * tup2[1]))
    return max_product