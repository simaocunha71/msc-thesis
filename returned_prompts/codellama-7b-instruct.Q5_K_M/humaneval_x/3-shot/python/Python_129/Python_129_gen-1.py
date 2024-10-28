    def bfs(grid, k):
        n = len(grid)
        m = len(grid[0])

        queue = deque([(0, 0, 0)])

        visited = set()

        res = []

        while queue:
            i, j, cnt = queue.popleft()

            if cnt == k:
                res.append(grid[i][j])
                continue

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj

                if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    queue.append((ni, nj, cnt + 1))

        return res

    return bfs(grid, k)
