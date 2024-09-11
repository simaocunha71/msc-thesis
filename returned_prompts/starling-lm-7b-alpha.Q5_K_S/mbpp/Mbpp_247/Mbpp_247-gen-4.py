def lps(s):
    n = len(s)
    lps = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        lps[i][i] = 1

    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n):
            if s[i] == s[j] and (i + 1 == j or lps[i + 1][j - 1]):
                lps[i][j] = 2 + lps[i + 1][j - 1]
            else:
                lps[i][j] = max(lps[i + 1][j], lps[i][j - 1])

    return lps[0][n - 1]


# assert lps("TENS FOR TENS") == 5

def lps(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n):
            if s[i] == s[j] and (i + 1 == j or dp[i + 1][j - 1]):
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


# assert lps("TENS FOR TENS") == 5

def lps(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 1, 0, -1):
        for