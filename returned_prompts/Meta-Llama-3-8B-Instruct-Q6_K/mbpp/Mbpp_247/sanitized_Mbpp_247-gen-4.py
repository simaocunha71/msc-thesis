def lps(s):
    s = s.lower()
    n = len(s)
    L = [[0 for x in range(n)]for x in range(n)]
    L[0][0] = 1
    for i in range(1, n):
        L[i][i] = 1
    for i in range(2, n):
        for j in range(i):
            if s[i] == s[j]:
                L[i][j] = L[i-1][j-1] + 2
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    return L[n-1][n-1]