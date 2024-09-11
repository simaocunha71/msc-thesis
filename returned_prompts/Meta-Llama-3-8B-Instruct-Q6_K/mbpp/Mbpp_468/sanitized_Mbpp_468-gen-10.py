def max_product(nums):
    max_product = [0]*len(nums)
    max_product[0] = nums[0]
    for i in range(1, len(nums)):
        max_product[i] = max(nums[i], max_product[i-1]*nums[i])
    return max(max_product)  # Return the maximum product