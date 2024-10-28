def unique_product(lst):
    if not lst:
        return 1
    unique_nums = list(set(lst))
    product = 1
    for num in unique_nums:
        if num == 0:
            return 0
        product *= num
    return product