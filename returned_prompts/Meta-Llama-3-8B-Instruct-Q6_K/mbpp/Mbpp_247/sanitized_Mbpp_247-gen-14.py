def lps(s):
    n = len(s)
    table = [[0 for x in range(n)]for x in range(n)]
    L = 0
    for i in range(n):
        table[i][i] = 1
    for cl in range(2, n):
        for i in range(n - cl):
            j = i + cl
            if s[i] == s[j] and cl == 2:
                table[i][j] = 2
            elif s[i] == s[j]:
                table[i][j] = table[i + 1][j - 1] + 2
            else:
                table[i][j] = max(table[i][j - 1], table[i + 1][j])
    return table[0][n - 1]