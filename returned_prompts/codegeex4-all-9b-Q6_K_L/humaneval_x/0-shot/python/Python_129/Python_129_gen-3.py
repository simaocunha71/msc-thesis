def minPath(grid, k):
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = collections.deque()
    visited = set()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                q.append((i, j, 0))
                visited.add((i, j, 0))
    while q:
        i, j, steps = q.popleft()
        if steps == k:
            return [grid[i][j]]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and (ni, nj, steps + 1) not in visited:
                q.append((ni, nj, steps + 1))
                visited.add((ni, nj, steps + 1))
    return []