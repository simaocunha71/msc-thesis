"""
dp = [[] for _ in range(len(s))]
for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i] == s[j]:
            if j - i == 1:
                dp[i][j] = True
            else:
                dp[i][j] = dp[i + 1][j - 1]
        else:
            dp[i][j] = False
return max(dp[i][j] for i in range(len(s)) for j in range(i, len(s)))
"""
