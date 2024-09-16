def lps(s):
    # s = "TENS FOR TENS"
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    max_len = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = 2
            else:
                dp[i][j] = 1
            max_len = max(max_len, dp[i][j])
    return max_len