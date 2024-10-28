
def max_product(nums: list) -> int:
    max_product = 1
    max_ending_here = 1
    for i in range(len(nums)):
        max_ending_here *= nums[i]
        if max_ending_here < 0:
            max_ending_here = 1
        max_product = max(max_product, max_ending_here)
    return max_product


