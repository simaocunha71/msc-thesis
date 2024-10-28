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