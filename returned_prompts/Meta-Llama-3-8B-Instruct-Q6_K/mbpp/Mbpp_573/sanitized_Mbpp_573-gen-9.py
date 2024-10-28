def unique_product(nums):
    unique_nums = set(nums)
    product = 1
    for num in unique_nums:
        product *= num
    return product