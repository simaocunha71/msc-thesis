
def max_sum(nums):
    n = len(nums)
    dp = [nums[0]]
    for i in range(1, n):
        dp.append(max(dp[i-1]+nums[i], nums[i]))
    return max(dp)


