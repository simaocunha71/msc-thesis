def lps(s):
    n = len(s)
    m = [[0 for x in range(n)]for x in range(n)]
    L = 0
    for i in range(n):
        m[i][i] = 1
    for cl in range(2, n):
        for i in range(n-cl):
            j = i+cl
            if s[i] == s[j]:
                m[i][j] = 2 + m[i+1][j-1]
                if cl == 1:
                    L = cl
                elif m[i][j] > L:
                    L = m[i][j]
            else:
                m[i][j] = max(m[i+1][j], m[i][j-1])
    return L