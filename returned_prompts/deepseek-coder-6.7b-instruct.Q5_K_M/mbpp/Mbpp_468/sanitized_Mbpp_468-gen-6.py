def max_product(nums):
    max_prod = [0]*len(nums)
    max_prod[0] = nums[0]
    for i in range(1, len(nums)):
        max_prod[i] = max(nums[i], max_prod[i-1]*nums[i])
    return max(max_prod)