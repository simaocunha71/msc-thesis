def unique_product(lst):
    unique_nums = set(lst)
    product = 1
    for num in unique_nums:
        product *= num
    return product

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))  # 720000000


"""
