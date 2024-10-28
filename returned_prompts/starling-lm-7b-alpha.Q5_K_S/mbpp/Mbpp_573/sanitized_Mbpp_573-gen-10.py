def unique_product(lst):
    unique_lst = list(set(lst))
    product = 1
    for i in unique_lst:
        product *= i
    return product