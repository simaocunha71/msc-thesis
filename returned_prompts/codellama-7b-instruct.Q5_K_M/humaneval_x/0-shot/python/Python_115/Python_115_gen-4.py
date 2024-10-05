
def max_fill(grid, capacity):
    from itertools import product
    from collections import deque

    # init
    m, n = len(grid), len(grid[0])
    visited = [[0] * n for _ in range(m)]
    queue = deque([])

    # BFS
    for i in range(m):
        for j in range(n):
            if grid[i][j] and not visited[i][j]:
                queue.append((i, j, 0))
                visited[i][j] = 1
    while queue:
        i, j, level = queue.popleft()
        if level == capacity:
            continue
        for di, dj in product([-1, 0, 1], repeat=2):
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n:
                if grid[ni][nj] and not visited[ni][nj]:
                    queue.append((ni, nj, level + 1))
                    visited[ni][nj] = 1

    return sum([1 for i in range(m) for j in range(n) if grid[i][j] and visited[i][j]])
