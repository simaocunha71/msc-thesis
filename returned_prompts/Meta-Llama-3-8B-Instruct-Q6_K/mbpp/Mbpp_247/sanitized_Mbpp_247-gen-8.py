def lps(s):
    n = len(s)
    table = [[0 for x in range(n)]for x in range(n)]
    L = 0
    for i in range(n):
        table[i][i] = 1
    start = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            L += 2
            start = i
            table[i][i+1] = 1
        else:
            table[i][i+1] = 0
    for k in range(3, n+1):
        for i in range(n-k+1):
            j = i+k-1
            if s[i] == s[j]:
                table[i][j] = table[i+1][j-1] + 2
                if table[i][j] > L:
                    L = table[i][j]
                    start = i
            else:
                table[i][j] = max(table[i+1][j], table[i][j-1])
    return L