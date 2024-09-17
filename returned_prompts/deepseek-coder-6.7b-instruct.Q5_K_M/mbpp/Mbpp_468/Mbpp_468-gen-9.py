
def max_product(nums):
    if len(nums) < 2:
        return None

    max_prod = nums[0] * nums[1]
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            max_prod = max(max_prod, nums[i] * nums[j])

    return max_prod


