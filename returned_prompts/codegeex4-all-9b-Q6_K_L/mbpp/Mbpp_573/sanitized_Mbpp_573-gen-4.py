def unique_product(lst):
    unique_lst = list(set(lst))
    product = 1
    for num in unique_lst:
        product *= num
    return product