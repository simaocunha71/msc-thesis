def lps(s):
    n = len(s)
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        table[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                table[i][j] = table[i + 1][j - 1] + 2
            else:
                table[i][j] = max(table[i + 1][j], table[i][j - 1])
    return table[0][n - 1]