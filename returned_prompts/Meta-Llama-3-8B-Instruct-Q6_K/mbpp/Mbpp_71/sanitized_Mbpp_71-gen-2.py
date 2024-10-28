from random import randint
def comb_sort(nums):
    gap = len(nums)
    shrink = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink)
        swapped = False

        for i in range(len(nums) - gap):
            j = i + gap
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                swapped = True

    return nums