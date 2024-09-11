def is_product_even(lst):
    prod = 1
    for item in lst:
        prod *= item
    return prod % 2 == 0