def catalan_number(n):
    res = [[0 for i in range(n+1)] for j in range(n+1)]
    res[0][0] = 1
    for i in range(1, n+1):
        for j in range(i+1):
            if j == 0 or j == i:
                res[i][j] = 1
            else:
                res[i][j] = res[i-1][j-1] + res[i-1][j]
    return res[n][n]

