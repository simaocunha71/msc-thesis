def lps(s):
    n = len(s)
    table = [[0 for x in range(n)]for x in range(n)]
    L = 0
    for i in range(n):
        table[i][i] = 1
    start = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            table[i][i+1] = 2
            start = i
            L = 2
        else:
            table[i][i+1] = 1
    for k in range(3, n+1):
        for i in range(n-k+1):
            j = i+k-1
            if s[i] == s[j] and table[i+1][j-1] > 0:
                table[i][j] = table[i+1][j-1]+2
                if k == L:
                    start = i
                L = max(L, k)
            else:
                table[i][j] = max(table[i][j-1], table[i+1][j])
    return L