"""
def two_unique_nums(nums):
    unique_nums = []
    for i in range(len(nums)):
        if nums[i] not in unique_nums:
            unique_nums.append(nums[i])
    return unique_nums

print(two_unique_nums([1,2,3,2,3,4,5]))
"""

