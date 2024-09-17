def max_sum(nums:list)->int:
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(2)]
    for i in range(n):
        dp[i % 2][i] = nums[i]
    for i in range(1,n):
        for j in range(i):
            dp[(i+1)%2][j] = max(dp[i%2][j], dp[(i+1)%2][j+1]+nums[j])
            dp[(i+1)%2][i] = max(dp[i%2][i], dp[(i+1)%2][j]+nums[i])
    return dp[n%2][0]