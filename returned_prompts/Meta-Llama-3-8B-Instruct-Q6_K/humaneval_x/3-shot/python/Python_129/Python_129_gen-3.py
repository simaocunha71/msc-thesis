    def dfs(i, j, k, path, visited):
        if k == 0:
            return path
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited:
                visited.add((x, y))
                path.append(grid[x][y])
                res = dfs(x, y, k-1, path, visited)
                if res:
                    return res
                path.pop()
                visited.remove((x, y))
        return None

    min_path = float('inf')
    res = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            path = [grid[i][j]]
            visited = {(i, j)}
            result = dfs(i, j, k-1, path, visited)
            if result and len(result) < min_path:
                min_path = len(result)
                res = result
    return res


