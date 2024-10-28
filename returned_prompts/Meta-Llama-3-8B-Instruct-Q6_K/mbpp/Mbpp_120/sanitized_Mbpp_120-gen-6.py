def max_product_tuple(nums):
    return max([abs(a*b) for a, b in nums]) if len(nums) > 0 else 0