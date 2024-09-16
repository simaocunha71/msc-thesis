def max_product(nums):
    if len(nums) == 1:
        return nums[0]
    max_product = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max_product:
            max_product = nums[i]
    for i in range(1, len(nums)):
        for j in range(i, len(nums)):
            if nums[i] * nums[j] > max_product:
                max_product = nums[i] * nums[j]
    return max_product