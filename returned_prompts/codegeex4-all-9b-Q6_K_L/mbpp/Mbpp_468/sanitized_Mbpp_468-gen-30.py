def max_product(nums):
    product = 1
    for i in range(len(nums)):
        product *= nums[i]
    return product