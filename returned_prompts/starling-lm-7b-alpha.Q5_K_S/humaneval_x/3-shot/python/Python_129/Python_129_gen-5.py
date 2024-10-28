    def path_to(i, j, visited):
        res = []
        stack = [(i, j)]
        while stack:
            i, j = stack.pop()
            if grid[i][j] in visited:
                continue
            visited.add(grid[i][j])
            res.append(grid[i][j])
            for di, dj in zip([-1, 0, 1], [0, 1, 0]):
                if 0 <= i + di < n and 0 <= j + dj < n:
                    stack.append((i + di, j + dj))
        return res

    def solve(grid, k):
        n = len(grid)
        visited = set()
        min_path = None
        for i in range(n):
            for j in range(n):
                if grid[i][j] in visited:
                    continue
                path = path_to(i, j, visited)
                if len(path) == k:
                    if min_path == None:
                        min_path = path
                    elif path < min_path:
                        min_path = path
                else:
                    for idx in range(k - len(path)):
                        visited.add(grid[path[-1 + idx]][path[idx]])
        return min_path

    grid = [list(map(int, input_line.split(" "))) for input_line in grid]
    return solve(grid, k)


