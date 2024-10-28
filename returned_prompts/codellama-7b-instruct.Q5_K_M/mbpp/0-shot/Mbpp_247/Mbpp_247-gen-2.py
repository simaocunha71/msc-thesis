
def lps(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    max_len = 0
    for i in range(n):
        dp[i][i] = 1
        max_len = max(max_len, 1)
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 2
            max_len = max(max_len, 2)
    for k in range(2, n):
        for i in range(n - k):
            j = i + k
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return max_len
