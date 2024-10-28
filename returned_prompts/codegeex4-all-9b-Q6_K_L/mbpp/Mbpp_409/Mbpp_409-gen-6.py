def min_product_tuple(test_list):
    product_list = [a*b for a,b in test_list]
    min_product = min(product_list)
    return min_product

