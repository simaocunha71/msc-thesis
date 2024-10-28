def lps(s):
    n = len(s)

    # Create a 2D array to store the length of the longest palindromic subsequence
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill the dp array
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1):
        dp[i][i + 1] = 2 if s[i] == s[i + 1] else 1
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]