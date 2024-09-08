def unique_product(lst):
    product = 1
    for i in set(lst):
        product *= i
    return product