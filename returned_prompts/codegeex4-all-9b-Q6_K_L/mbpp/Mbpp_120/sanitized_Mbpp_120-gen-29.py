def max_product_tuple(tuples: list) -> int:
    products = [abs(a*b) for a,b in tuples]
    return max(products)