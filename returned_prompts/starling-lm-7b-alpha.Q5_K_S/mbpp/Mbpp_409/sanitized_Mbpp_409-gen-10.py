def min_product_tuple(l):
    products = [a * b for a, b in l]
    return min(products)