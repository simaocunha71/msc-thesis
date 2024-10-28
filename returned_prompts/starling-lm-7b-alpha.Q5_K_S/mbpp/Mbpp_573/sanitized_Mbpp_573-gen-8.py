def unique_product(nums):
    product = 1
    nums_set = set(nums)
    for n in nums_set:
        product *= n
    return product