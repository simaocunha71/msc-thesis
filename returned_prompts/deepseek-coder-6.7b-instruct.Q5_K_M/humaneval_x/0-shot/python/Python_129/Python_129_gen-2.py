
    def minPath(grid, k):
        n = len(grid)
        dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]
        visited = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        def dfs(x, y, z):
            if z == k:
                return grid[x][y]
            if visited[x][y][z]:
                return dp[x][y][z]
            visited[x][y][z] = 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    dp[x][y][z] = min(dp[x][y][z], dfs(nx, ny, z + 1) + grid[x][y])
            return dp[x][y][z]

        min_path = float('inf')
        min_point = ()
        for i in range(n):
            for j in range(n):
                cur_min_path = dfs(i, j, 0)
                if cur_min_path < min_path:
                    min_path = cur_min_path
                    min_point = (i, j)
        path = []
        x, y, z = min_point[0], min_point[1], 0
        while z < k:
            path.append(grid[x][y])
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < n and dp[nx][ny][z + 1] + grid[x][y] == dp[x][y][z]:
                    x, y = nx, ny
                    z += 1