def comb_sort(nums):
    def gap(g):
        if g > len(nums) // 1.3:
            return len(nums) // 2
        elif g < 1:
            return 1
        else:
            return int(g * 1.3)

    n = len(nums)
    g = n
    swapped = True
    while g > 1 or swapped:
        g = gap(g)
        swapped = False
        for i in range(n - g):
            if nums[i] > nums[i + g]:
                nums[i], nums[i + g] = nums[i + g], nums[i]
                swapped = True
    return nums