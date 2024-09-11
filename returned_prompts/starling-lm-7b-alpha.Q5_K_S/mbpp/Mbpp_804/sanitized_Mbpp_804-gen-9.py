def is_product_even(nums):
    if len(nums) == 0:
        return False
    p = 1
    for i in nums:
        p *= i
    return p % 2 == 0