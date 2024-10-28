    m = len(grid)
    n = len(grid[0])

    visited = [[False for _ in range(n)] for _ in range(m)]
    queue = [[(0, 0, 0)]]
    ans = []

    while queue:
        cell = queue.pop(0)
        i, j, steps = cell
        visited[i][j] = True
        ans.append(grid[i][j])
        if steps == k:
            return ans

        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                queue.append((x, y, steps+1))


    return ans