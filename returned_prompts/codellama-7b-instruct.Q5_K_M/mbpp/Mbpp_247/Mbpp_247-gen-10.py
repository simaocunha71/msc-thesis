"""
def lps(s):
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            if s[i - 1] == s[j - 1] and j - i < 2:
                dp[i] = max(dp[i], dp[j - i] + 1)
            elif s[i - 1] == s[j - 1] and j - i > 2 and dp[i] <= dp[j - i]:
                dp[i] = dp[j - i] + 1
    return dp[n]
"""
