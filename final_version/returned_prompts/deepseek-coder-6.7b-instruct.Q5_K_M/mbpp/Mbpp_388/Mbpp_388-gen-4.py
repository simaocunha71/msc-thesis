def product_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

print(product_list([1, 2, 3, 