def max_product(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0

    def max_product_sub(nums, i):
        if i == 0:
            return nums[i]
        if i == 1:
            if nums[i-1] >= 0:
                return max(nums[i], nums[i]*nums[i-1])
            else:
                return nums[i]
        if i > 1:
            if nums[i-2] >= 0 and nums[i-1] >= 0:
                return max(nums[i], nums[i]*nums[i-1]*nums[i-2])
            elif nums[i-2] < 0 and nums[i-1] < 0:
                return max(nums[i], nums[i]*nums[i-1]*nums[i-2])
            else:
                return max(nums[i], nums[i-1]*nums[i])

    return max(max_product_sub(nums, i) for i in range(len(nums)))