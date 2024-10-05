
def minSubArraySum(nums):
    min_sum = float('inf')
    cur_sum = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        min_sum = min(min_sum, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return min_sum


