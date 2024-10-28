def unique_product(nums):
    product = 1
    unique_nums = set(nums)
    for num in unique_nums:
        product *= num
    return product