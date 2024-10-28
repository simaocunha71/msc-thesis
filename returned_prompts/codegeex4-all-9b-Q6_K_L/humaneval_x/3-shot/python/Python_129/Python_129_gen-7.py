    def dfs(x, y, depth, path, visited):
        if depth == k:
            return path

        visited.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                result = dfs(nx, ny, depth + 1, path + [grid[nx][ny]], visited)
                if result:
                    return result
                visited.remove((nx, ny))

        visited.remove((x, y))

    n = len(grid)
    visited = set()
    result = dfs(0, 0, 0, [grid[0][0]], visited)

    return result

