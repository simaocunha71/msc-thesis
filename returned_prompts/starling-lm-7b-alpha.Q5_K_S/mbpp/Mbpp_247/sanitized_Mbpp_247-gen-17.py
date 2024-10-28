def lps(s):
    dp = [[0 for j in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    for sublen in range(2, len(s) + 1):
        for i in range(len(s)):
            j = i + sublen - 1
            if j >= len(s):
                break
            if s[i] == s[j] and sublen == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    return dp[0][-1]