def comb_sort(nums: list) -> list:
    gap = len(nums) // 2
    while gap > 1:
        for i in range(gap, len(nums)):
            if nums[i] < nums[i - gap]:
                nums[i], nums[i - gap] = nums[i - gap], nums[i]
        gap //= 2
    return nums