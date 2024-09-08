def unique_product(lst):
    unique_numbers = set(lst)
    product = 1
    for num in unique_numbers:
        product *= num
    return product