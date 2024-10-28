def unique_product(nums):
    num_set = set(nums)
    product = 1
    for num in num_set:
        product *= num
    return product