    n = len(grid)
    dp = [ [ [float('inf')] * (k+1) for _ in range(n) ] for _ in range(n) ]

    # Initialize dp for the first row and column
    for i in range(n):
        dp[i][0][0] = grid[i][0]
        dp[0][i][0] = grid[0][i]

    for i in range(1, n):
        for j in range(1, n):
            for l in range(1, k+1):
                dp[i][j][l] = min(dp[i-1][j][l-1], dp[i][j-1][l-1]) + grid[i][j]

    # Find the minimum path
    min_path = []
    i, j, l = n-1, n-1, k
    while i > 0 and j > 0 and l > 0:
        min_path.append(grid[i][j])
        if dp[i-1][j][l-1] < dp[i][j-1][l-1]:
            i -= 1
        else:
            j -= 1
        l -= 1

    min_path.append(grid[0][0])
    min_path.reverse()

    return min_path

