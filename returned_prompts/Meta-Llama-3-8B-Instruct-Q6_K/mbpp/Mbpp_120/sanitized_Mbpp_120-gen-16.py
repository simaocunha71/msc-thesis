def max_product_tuple(lst):
    max_product = float('-inf')
    for t in lst:
        for p in [(t[0], t[1]), (t[1], t[0])]:
            product = p[0] * p[1]
            max_product = max(max_product, product)
    return max_product