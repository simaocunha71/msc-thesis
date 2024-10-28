
def lps(s):
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(i, n+1):
            if i == j:
                dp[i][j] = 1
            elif i+1 == j:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n]


