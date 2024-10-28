def comb_sort(nums:list):
    n = len(nums)
    gap = n
    swapped = True
    while gap != 0 or swapped == True:
        gap = gap//2
        swapped = False
        for i in range(0, n-gap):
            if nums[i] > nums[i+gap]:
                nums[i], nums[i+gap] = nums[i+gap], nums[i]
                swapped = True
    return nums