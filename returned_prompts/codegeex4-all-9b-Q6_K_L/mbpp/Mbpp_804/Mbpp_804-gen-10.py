def is_product_even(nums):
    return all(x % 2 == 0 for x in nums) or len(nums) == 0

