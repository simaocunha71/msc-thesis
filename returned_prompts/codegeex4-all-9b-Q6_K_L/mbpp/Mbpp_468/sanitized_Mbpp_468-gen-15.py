def max_product(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] * nums[j] > nums[i]:
                nums[i] = nums[i] * nums[j]
    return max(nums)