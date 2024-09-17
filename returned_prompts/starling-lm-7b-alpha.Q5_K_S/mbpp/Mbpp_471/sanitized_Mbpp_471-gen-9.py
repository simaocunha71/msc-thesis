def find_remainder(nums, n):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        dp[i] = (dp[i-1] * nums[i]) % n
    return (reduce(lambda x,y: (x*y)%n, dp)) % n