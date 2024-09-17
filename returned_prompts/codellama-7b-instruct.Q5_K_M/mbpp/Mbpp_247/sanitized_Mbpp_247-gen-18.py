def lps(s):
    n = len(s)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]