def comb_sort(nums: list) -> list:
    gap = len(nums)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        j = 0
        while j + gap < len(nums):
            if nums[j] > nums[j + gap]:
                nums[j], nums[j + gap] = nums[j + gap], nums[j]
                sorted = False
            j += 1
    return nums