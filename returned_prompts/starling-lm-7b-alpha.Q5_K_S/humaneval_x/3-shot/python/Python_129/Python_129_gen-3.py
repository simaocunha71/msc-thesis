    def dfs(grid, k, x, y, visited, curr_path):
        if k == 0:
            return curr_path
        if (x, y) in visited:
            return []

        visited.add((x, y))
        curr_path.append(grid[x][y])
        min_path = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                min_path = min(min_path, dfs(grid, k - 1, x + dx, y + dy, visited, curr_path))
        visited.remove((x, y))
        curr_path.pop()
        return min_path

    def minPath(grid, k):
        if k == 0:
            return []
        return min(dfs(grid, k, i, j, set(), []) for i in range(len(grid)) for j in range(len(grid[0])))


