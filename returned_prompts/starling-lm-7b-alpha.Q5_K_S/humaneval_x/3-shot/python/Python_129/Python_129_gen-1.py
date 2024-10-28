    def minPathHelper(grid, k, x, y, visited, lst):
        if k == 0:
            return lst

        if (x, y) in visited:
            return []

        visited.add((x, y))
        lst.append(grid[x][y])

        minPath = []
        if x > 0 and k >= 2:
            minPath = min(minPath, minPathHelper(grid, k - 1, x - 1, y, visited, lst))
        if y > 0 and k >= 2:
            minPath = min(minPath, minPathHelper(grid, k - 1, x, y - 1, visited, lst))
        if x < len(grid) - 1 and k >= 2:
            minPath = min(minPath, minPathHelper(grid, k - 1, x + 1, y, visited, lst))
        if y < len(grid[0]) - 1 and k >= 2:
            minPath = min(minPath, minPathHelper(grid, k - 1, x, y + 1, visited, lst))

        return minPath

    visited = set()
    minPath = minPathHelper(grid, k, 0, 0, visited, [])
    return minPath


