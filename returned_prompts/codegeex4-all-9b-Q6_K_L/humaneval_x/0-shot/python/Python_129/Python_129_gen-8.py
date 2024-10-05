def minPath(grid, k):
    def dfs(x, y, k, path):
        if k == 0:
            return path
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return None
        res = None
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_path = dfs(x+dx, y+dy, k-1, path+[grid[x][y]])
            if new_path:
                if res is None or new_path < res:
                    res = new_path
        return res
    return dfs(0, 0, k, [])