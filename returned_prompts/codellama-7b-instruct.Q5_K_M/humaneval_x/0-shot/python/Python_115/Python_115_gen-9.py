
    def max_fill(grid, capacity):
        from collections import deque
        from math import floor, ceil
        m, n = len(grid), len(grid[0])
        buckets = deque([(0, 0, 0)])
        visited = set()
        while buckets:
            i, j, t = buckets.popleft()
            if i == m-1:
                return t
            visited.add((i, j))
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ii, jj = i + di, j + dj
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] and (ii, jj) not in visited:
                    buckets.append((ii, jj, t + 1))
                    grid[ii][jj] = 0
        return -1



