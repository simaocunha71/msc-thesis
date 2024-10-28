
def minPath(grid, k):
    N = len(grid)
    graph = [set() for _ in range(N * N + 1)]
    for i in range(N):
        for j in range(N):
            graph[grid[i][j]].add((i, j))
    visited = [False] * (N * N + 1)
    queue = [(1, 0)]
    while queue:
        node, step = queue.pop(0)
        if visited[node]:
            continue
        visited[node] = True
        if step == k:
            return [grid[i][j] for i, j in graph[node]]
        for n in graph[node]:
            queue.append((n, step + 1))
    return []


