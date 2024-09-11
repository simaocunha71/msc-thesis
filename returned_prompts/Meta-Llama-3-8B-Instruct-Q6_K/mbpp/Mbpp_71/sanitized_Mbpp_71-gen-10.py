def comb_sort(nums):
    n = len(nums)
    gap = n
    shrink = 1.3
    sorted_nums = nums[:]
    swapped = True
    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap > 1:
            swapped = False
            for i in range(0, n - gap):
                j = i + gap
                if sorted_nums[i] > sorted_nums[j]:
                    sorted_nums[i], sorted_nums[j] = sorted_nums[j], sorted_nums[i]
                    swapped = True
        else:
            gap = 1
    return sorted_nums