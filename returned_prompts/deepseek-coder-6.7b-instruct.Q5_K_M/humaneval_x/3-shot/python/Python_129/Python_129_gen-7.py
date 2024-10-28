    import heapq
    n = len(grid)
    pq, visited, res = [], set(), []
    for i in range(n):
        for j in range(n):
            pq.append((grid[i][j], i, j))
    heapq.heapify(pq)

    while len(res) < k:
        val, i, j = heapq.heappop(pq)
        if (i, j) not in visited:
            res.append(val)
            visited.add((i, j))
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + x, j + y
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                    heapq.heappush(pq, (grid[ni][nj], ni, nj))
    return res


