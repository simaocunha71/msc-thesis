def min_product_tuple(lst):
    min_product = float('inf')
    for i in lst:
        product = i[0]*i[1]
        if product < min_product:
            min_product = product
    return min_product