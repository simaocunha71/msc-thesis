    N = len(grid)
    visited = [[False] * N for _ in range(N)]
    res = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j, k, path):
        if k == 0:
            res = path[:]
            return
        visited[i][j] = True
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                dfs(ni, nj, k - 1, path + [grid[ni][nj]])
        visited[i][j] = False

    for i in range(N):
        for j in range(N):
            dfs(i, j, k, [grid[i][j]])
    return res
