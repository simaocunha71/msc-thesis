def is_product_even(l):
    product = 1
    for num in l:
        product *= num
    return product % 2 == 0