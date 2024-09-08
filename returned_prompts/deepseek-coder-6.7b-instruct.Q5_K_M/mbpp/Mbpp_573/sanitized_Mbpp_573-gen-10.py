def unique_product(lst):
    unique_numbers = set(lst)
    product = 1
    for number in unique_numbers:
        product *= number
    return product