def largest_subset(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] * 2 == nums[j]:
            i += 1
            j += 1
        else:
            j += 1
    return i + 1


# Time:  O(nlogn)
# Space: O(1)

# optimized from O(n^2) to O(nlogn)
# Reference:
# https://stackoverflow.com/questions/40390269/find-the-length-of-largest-contiguous-subset-with-given-property/40391076#40391076


"""
Given an array of numbers, find the size of the largest subset of the array so that every number is divisible by some number in the subset.
For example, given the array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], the largest subset is [2, 4, 8, 16] and its size is 4.

Assert: (largest_subset([1, 3, 6, 13, 17, 18])) == 4
"""


def largest_subset(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] * 2 == nums[j]:
            i += 1
            j += 1
        else:
            j += 1
    return i + 1


# Time:  O(nlogn)
# Space