def unique_product(lst):
    unique_list = list(set(lst))
    product = 1
    for num in unique_list:
        product *= num
    return product