def unique_product(lst):
    unique_nums = list(set(lst))
    product = 1
    for num in unique_nums:
        product *= num
    return product