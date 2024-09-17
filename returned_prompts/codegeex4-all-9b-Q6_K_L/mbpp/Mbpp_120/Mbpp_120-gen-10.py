def max_product_tuple(lst: list) -> int:
    max_product = 0
    for tup1 in lst:
        for tup2 in lst:
            product = abs(tup1[0] * tup2[0]) + abs(tup1[1] * tup2[1])
            if product > max_product:
                max_product = product
    return max_product

