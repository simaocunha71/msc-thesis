
def lps(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                dp[i][j] = (s[i] == s[j]) + dp[i + 1][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] + 1 if s[i] == s[j] else 0

    return dp[0][n - 1]


