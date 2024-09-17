
def max_product_tuple(lst):
    products = [abs(a*b) for (a, b) in lst]
    return max(products)


