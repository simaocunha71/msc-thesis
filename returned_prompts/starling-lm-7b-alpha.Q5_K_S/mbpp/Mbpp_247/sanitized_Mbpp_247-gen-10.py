def lps(s):
    dp = [[0 for j in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    for i in range(len(s)-1, 0, -1):
        for j in range(i, len(s)):
            if s[i-1] == s[j]:
                dp[i-1][j] = dp[i][j] + 1
            else:
                dp[i-1][j] = max(dp[i][j], dp[i-1][j-1])
    return dp[0][-1]