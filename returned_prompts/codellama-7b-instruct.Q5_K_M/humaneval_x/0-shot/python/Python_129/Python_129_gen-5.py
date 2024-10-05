
def minPath(grid, k):
    n = len(grid)
    m = len(grid[0])
    graph = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                graph[i][j] = grid[i][j]

    def dfs(x, y, k, visited, path):
        if k == 0:
            return 0
        if x < 0 or x >= n or y < 0 or y >= m:
            return 1 << 31
        if grid[x][y] == 0:
            return 1 << 31

        visited[x][y] = True
        path.append(grid[x][y])
        k -= 1

        min_val = 1 << 31
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if not visited[new_x][new_y] and not (new_x < 0 or new_x >= n or new_y < 0 or new_y >= m):
                min_val = min(min_val, dfs(new_x, new_y, k, visited, path))
        visited[x][y] = False
        path.pop()

        return min_val

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[False] * m for _ in range(n)]
    path = []
    res = dfs(0, 0, k, visited, path)
    return path

B:

def minPath(grid, k):
    n = len(grid)
    m = len(grid[0])
    graph = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                graph[i][j] = grid[i][j]
