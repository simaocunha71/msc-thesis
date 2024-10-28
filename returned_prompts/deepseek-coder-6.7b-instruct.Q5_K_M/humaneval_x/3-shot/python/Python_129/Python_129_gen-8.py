    N = len(grid)
    INF = float('inf')
    dp = [[[INF] * (k + 1) for _ in range(N)] for _ in range(N)]
    dp[0][0][0] = grid[0][0]

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for c in range(1, k + 1):
        q = [(grid[0][0], 0, 0)]
        seen = [[False] * N for _ in range(N)]
        seen[0][0] = True
        while q:
            val, x, y = heapq.heappop(q)
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not seen[nx][ny]:
                    seen[nx][ny] = True
                    if dp[nx][ny][c - 1] > val + grid[nx][ny]:
                        dp[nx][ny][c] = dp[nx][ny][c - 1] = val + grid[nx][ny]
                        heapq.heappush(q, (dp[nx][ny][c], nx, ny))

    return dp[-1][-1][k:]


