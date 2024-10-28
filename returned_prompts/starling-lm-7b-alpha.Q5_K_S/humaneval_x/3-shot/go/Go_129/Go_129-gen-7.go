    def minpath(x, y, grid, k, cur, res):
        if k == 0: return res
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and cur + grid[nx][ny] in res:
                res = res[:k - 1] + [cur + grid[nx][ny]]
                k -= 1
                break
        return minpath(x, y, grid, k, cur + grid[x][y], res)

    n = len(grid)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    return minpath(0, 0, grid, k, grid[0][0], [grid[0][0]])
}



