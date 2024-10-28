
def lps(s: str) -> int:
    n = len(s)
    lps = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        lps[i][i] = 1
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                lps[i][j] = lps[i + 1][j - 1] + 2
            else:
                lps[i][j] = max(lps[i + 1][j], lps[i][j - 1])
    return lps[0][n - 1]


