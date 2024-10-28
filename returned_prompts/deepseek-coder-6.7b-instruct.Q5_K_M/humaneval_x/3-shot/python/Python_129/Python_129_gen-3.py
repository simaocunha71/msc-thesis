    n = len(grid)
    dp = [[[float('inf')]*k for _ in range(n)] for _ in range(n)]
    dp[0][0][0] = grid[0][0]
    moves = [(0,1),(0,-1),(-1,0),(1,0)]
    for s in range(1,n*n):
        for _ in range(s):
            i, j, l = _//n, _%n, _//n
            for move in moves:
                ni, nj = i+move[0], j+move[1]
                if 0<=ni<n and 0<=nj<n:
                    for p in range(l+1):
                        dp[ni][nj][_%n] = min(dp[ni][nj][_%n], dp[i][j][p]+grid[ni][nj])
    return min(dp[-1][-1])


