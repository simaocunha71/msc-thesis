
def minSubArraySum(nums):
    min_sum = float('inf')
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            min_sum = min(min_sum, curr_sum)
    return min_sum