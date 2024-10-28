"""
def largest_subset(nums):
    nums.sort()
    i = 0
    while i < len(nums) - 1:
        if nums[i] % nums[i+1] != 0:
            i += 1
        else:
            while i < len(nums) - 1 and nums[i] % nums[i+1] == 0:
                i += 1
    return i + 1
"""
