    def dfs(x, y, k, visited, path):
        if k == 0:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                visited.add((nx, ny))
                result = dfs(nx, ny, k - 1, visited, path + [grid[nx][ny]])
                if result:
                    return result
                visited.remove((nx, ny))
        return None

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            visited = set()
            visited.add((i, j))
            result = dfs(i, j, k - 1, visited, [grid[i][j]])
            if result:
                return result

    return None

