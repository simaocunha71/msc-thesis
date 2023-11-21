
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    
    if len(nums) < 2:
        return nums[0]
    return min(*(min(nums[i: i + len(nums)] for i in range(-len(nums), -1)) if sum(nums[i: i+len(nums)]) >= 0 else [None]) + [i, nums[-1]]
         for i in range(len(nums)-2,-1,-1))
