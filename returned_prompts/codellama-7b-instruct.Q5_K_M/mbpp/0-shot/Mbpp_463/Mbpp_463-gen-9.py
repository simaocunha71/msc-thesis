"""
def max_subarray_product(nums):
    if not nums:
        return None
    max_product = nums[0]
    for i in range(1, len(nums)):
        max_product = max(max_product, max_product * nums[i], nums[i])
    return max_product
"""

