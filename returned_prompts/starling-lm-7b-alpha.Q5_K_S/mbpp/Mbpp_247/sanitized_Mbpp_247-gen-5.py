def lps(s):
    # Initialize DP table
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # Initialize base case
    for i in range(n):
        dp[i][i] = 1
    # Fill DP table
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]