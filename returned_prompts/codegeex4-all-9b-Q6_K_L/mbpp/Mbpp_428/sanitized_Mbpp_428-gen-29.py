def shell_sort(nums: list) -> list:
    length = len(nums)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap //= 2
    return nums