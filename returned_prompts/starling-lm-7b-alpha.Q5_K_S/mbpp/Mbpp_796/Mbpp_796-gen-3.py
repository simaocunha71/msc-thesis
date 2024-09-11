def return_product(d):
    product = 1
    if not d:
        return 1
    for k in d:
        product *= d[k]
    return product

# Testing
assert return_product({'a':