def catalan_number(n):
    catalan = [[0 for x in range(n+1)] for x in range(n+1)]
    catalan[0][0] = 1
    for i in range(1, n+1):
        for j in range(i+1):
            if j == 0 or j == i:
                catalan[i][j] = 1
            else:
                catalan[i][j] = catalan[i-1][j-1] + catalan[i-1][j]
    return catalan[n][0]