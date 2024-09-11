import random
def comb_sort(nums: list):
    def swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    gap = len(nums)
    shrink = 1.3

    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink)
        swapped = False

        for i in range(len(nums) - gap):
            j = i + gap

            if nums[i] > nums[j]:
                swap(i, j)
                swapped = True

    return nums