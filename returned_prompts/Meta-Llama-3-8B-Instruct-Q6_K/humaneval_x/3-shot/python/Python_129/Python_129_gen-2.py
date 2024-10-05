    N = len(grid)
    visited = [[False]*N for _ in range(N)]
    min_path = []
    min_path_sum = float('inf')

    def dfs(x, y, path, path_sum):
        nonlocal min_path, min_path_sum
        if len(path) > k:
            return
        if path_sum > min_path_sum:
            return
        if len(path) == k:
            if path_sum < min_path_sum:
                min_path_sum = path_sum
                min_path = path[:]
            return
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, path + [grid[nx][ny]], path_sum + grid[nx][ny])
                visited[nx][ny] = False

    for i in range(N):
        for j in range(N):
            visited[i][j] = True
            dfs(i, j, [grid[i][j]], grid[i][j])
            visited[i][j] = False

    return min_path


