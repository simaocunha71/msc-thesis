def bell_number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        dp = [0]* (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = sum(dp[0:i])
        return dp[n]