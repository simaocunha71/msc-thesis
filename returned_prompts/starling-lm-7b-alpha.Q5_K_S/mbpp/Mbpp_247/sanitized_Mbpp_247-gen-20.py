def lps(s):
    dp = [[0 for i in range(len(s))] for j in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    for l in range(2, len(s) + 1):
        for i in range(len(s) - l + 1):
            j = i + l - 1
            if s[i] == s[j] and l == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][-1]