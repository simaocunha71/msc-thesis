def lps(s):
    n = len(s)
    L = [[0 for x in range(n)]for x in range(n)]
    for i in range(n):
        L[i][i] = 1
    for cl in range(2, n):
        for i in range(n-cl):
            j = i+cl
            if s[i] == s[j]:
                L[i][j] = 2 + L[i+1][j-1]
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j])
    return L[0][n-1] // 2 + 1 if s[0] == s[n-1] else L[0][n-1] // 2