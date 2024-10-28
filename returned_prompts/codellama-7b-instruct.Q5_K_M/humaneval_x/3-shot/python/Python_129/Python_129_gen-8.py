    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = [(0, 0, 0)]

    while queue:
        x, y, step = queue.pop(0)
        visited[x][y] = True

        if step == k:
            result = []

            for i in range(rows):
                for j in range(cols):
                    if visited[i][j]:
                        result.append(grid[i][j])
            return result

        for x2, y2 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if x2 < 0 or x2 >= rows or y2 < 0 or y2 >= cols:
                continue
            if not visited[x2][y2]:
                queue.append((x2, y2, step + 1))

    return []


