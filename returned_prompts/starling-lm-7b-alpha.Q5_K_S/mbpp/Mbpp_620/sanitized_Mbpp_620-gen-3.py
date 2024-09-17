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