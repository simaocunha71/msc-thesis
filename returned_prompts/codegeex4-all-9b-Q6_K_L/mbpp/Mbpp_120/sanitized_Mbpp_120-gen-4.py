def max_product_tuple(lst):
    def product(a, b):
        return abs(a * b)
    max_product = 0
    for pair in lst:
        max_product = max(max_product, product(pair[0], pair[1]))
    return max_product