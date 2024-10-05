
    def minPath(grid, k):
        N = len(grid)
        INF = float('inf')
        dp = [[[INF] * (k+1) for _ in range(N)] for _ in range(N)]
        path = [[[''] * (k+1) for _ in range(N)] for _ in range(N)]
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(N):
            for j in range(N):
                dp[i][j][0] = grid[i][j]
                path[i][j][0] = str(grid[i][j])

        for steps in range(1, k):
            for x in range(N):
                for y in range(N):
                    for dx, dy in moves:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if dp[nx][ny][steps-1] + grid[x][y] < dp[x][y][steps]:
                                dp[x][y][steps] = dp[nx][ny][steps-1] + grid[x][y]
                                path[x][y][steps] = path[nx][ny][steps-1] + ' ' + str(grid[x][y])
        
        min_val = min(dp[i][j][k-1] for i in range(N) for j in range(N))
        return [int(i) for i in path[x][y][k-1] for x in range(N) for y in range(N) if dp[x][y][k-1] == min_val]


    print(minPath([[1,2,3],[4,5,6],[7,8,9]], 3))
    print(minPath([[5,9,3],[4,1,6],[7,8,2]], 1))

This solution works by using dynamic programming. For each cell (i, j) and for each