
def minPath(grid, k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: List[int]
    """
    N = len(grid)
    res = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                dfs(grid, i, j, k, res)
    return res

def dfs(grid, x, y, k, res):
    if k == 0:
        return
    grid[x][y] = 0
    if k == 1:
        res.append(grid[x][y])
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny]:
            dfs(grid, nx, ny, k - 1, res)
    grid[x][y] = 1
