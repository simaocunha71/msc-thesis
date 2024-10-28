
def max_Product(nums):
    if len(nums) < 2:
        return (nums[0], nums[0])
    max_product = (nums[0] * nums[1], nums[0] * nums[-1])
    for i in range(len(nums)-1):
        max_product = max(max_product, (nums[i] * nums[i + 1]), (nums[i] * nums[-1]))
    return max_product


