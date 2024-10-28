def max_product(nums):
    max_product = 1
    for num in nums:
        max_product *= num
    return max_product