
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    
    if len(nums) < 1:
        return None

    best_sum = float('inf')
    index = 0
    ans = 0
    for index in range(len(nums)):
        current_sum = sum([i for i in nums[index:]]) # Add all the elements that we haven't included yet and then find the minimum sum of any non-empty subarray of it
        if (current_sum < best_sum):
            ans = index + 1 if ans == None else ans - 1
            best_sum = current_sum
    return ans