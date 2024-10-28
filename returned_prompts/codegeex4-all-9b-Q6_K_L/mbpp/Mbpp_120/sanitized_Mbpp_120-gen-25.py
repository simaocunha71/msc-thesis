def max_product_tuple(lst: list) -> int:
    max_product = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            product = abs(lst[i][0] * lst[j][0]) + abs(lst[i][1] * lst[j][1])
            if product > max_product:
                max_product = product
    return max_product