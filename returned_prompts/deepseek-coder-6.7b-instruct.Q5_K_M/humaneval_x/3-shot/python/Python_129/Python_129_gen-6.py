    from heapq import heappush, heappop

    n = len(grid)
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    heap = [(grid[0][0], 0, 0, [grid[0][0]])]
    visited = set([(0, 0)])

    while heap:
        min_dist, x, y, path = heappop(heap)

        if len(path) == k:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                new_dist = grid[nx][ny]
                new_path = path + [new_dist]
                heappush(heap, (new_dist, nx, ny, new_path))
                visited.add((nx, ny))

    return []

