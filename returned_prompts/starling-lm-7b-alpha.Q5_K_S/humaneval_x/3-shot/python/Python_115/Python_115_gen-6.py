    n, m = len(grid), len(grid[0])
    cap = bucket_capacity
    ans = 0
    while True:
        cur = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    grid[i][j] = grid[i][j] - 1
                    cur += 1
                    if cur == cap:
                        ans += 1
                        cur = 0
        if cur == 0:
            break
        ans += 1
    return ans


