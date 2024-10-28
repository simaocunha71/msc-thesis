def min_product_tuple(lst):
    min_product = float('inf')
    for pair in lst:
        product = pair[0] * pair[1]
        if product < min_product:
            min_product = product
    return min_product