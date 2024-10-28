def comb_sort(nums):
    gap = len(nums)
    while gap > 1:
        gap = (gap * 10) // 13
        if gap == 9 or gap == 10:
            gap = 11
        for i in range(len(nums) - gap):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
    return nums