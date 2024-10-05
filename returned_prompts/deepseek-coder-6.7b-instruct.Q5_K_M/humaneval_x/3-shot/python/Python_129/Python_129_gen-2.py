    n = len(grid)
    dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]
    path = [[[''] * (k + 1) for _ in range(n)] for _ in range(n)]
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(x, y, k):
        if k == 0:
            return ''
        if dp[x][y][k] != float('inf'):
            return path[x][y][k]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                temp = dfs(nx, ny, k - 1) + ' ' + str(grid[x][y])
                if temp < path[x][y][k]:
                    path[x][y][k] = temp
                    dp[x][y][k] = dp[nx][ny][k - 1] + 1
        return path[x][y][k]

    min_val = float('inf')
    min_pos = (0, 0)
    for i in range(n):
        for j in range(n):
            temp = dfs(i, j, k)
            if len(temp.split()) < min_val:
                min_val = len(temp.split())
                min_pos = (i, j)
    return [int(x) for x in path[min_pos[0]][min_pos[1]][k].split()]


