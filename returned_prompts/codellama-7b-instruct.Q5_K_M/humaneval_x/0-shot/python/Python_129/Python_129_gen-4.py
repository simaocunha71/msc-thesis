
def minPath(grid, k):
    n = len(grid)
    d = [ [0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            d[i][j] = grid[i][j]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0 and j != 0:
                d[i][j] = min(d[i][j-1], d[i][j])
            elif j == 0 and i != 0:
                d[i][j] = min(d[i-1][j], d[i][j])
            else:
                d[i][j] = min(d[i-1][j], d[i][j-1], d[i][j])
    return d[n-1][n-1]
