def max_product_tuple(tuple_list: list) -> int:
    max_prod = 0
    for t1, t2 in zip(tuple_list, tuple_list[1:]):
        prod = abs(t1[0] - t2[0]) * abs(t1[1] - t2[1])
        if prod > max_prod:
            max_prod = prod
    return max_prod