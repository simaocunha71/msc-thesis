
def minSubArraySum(nums):
    min_sum = float('inf')
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            min_sum = min(min_sum, sum)
    return min_sum

