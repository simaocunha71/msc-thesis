def lps(s):
    n = len(s)
    table = [[0 for x in range(n)]for x in range(n)]
    L = 0
    i = 0
    while (i < n):
        if (s[i] == s[n - 1]):
            table[i][n - 1] = 1
            L = 1
        i = i + 1
    table[n - 1][n - 1] = 1
    for i in range(n - 2, -1, -1):
        if (s[i] == s[n - 1]):
            table[i][n - 1] = 1
            L = L + 1
        else:
            table[i][n - 1] = 0
    for i in range(1, n):
        table[i][i] = 1
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if (s[i] == s[j] and table[i + 1][j - 1]):
                table[i][j] = table[i + 1][j - 1] + 2
            else:
                table[i][j] = max(table[i][j - 1], table[i + 1][j])
    return table[0][n - 1] + L - 1