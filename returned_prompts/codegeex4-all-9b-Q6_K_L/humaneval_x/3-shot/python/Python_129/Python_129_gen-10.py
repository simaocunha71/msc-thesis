    from typing import List

    def minPath(grid: List[List[int]], k: int) -> List[int]:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        min_path = []

        def dfs(x, y, path):
            if len(path) > k:
                return
            visited.add((x, y))
            path.append(grid[x][y])

            if len(path) == k:
                if not min_path or path < min_path:
                    min_path = path
            else:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                        dfs(nx, ny, path)
            visited.remove((x, y))
            path.pop()

        for i in range(n):
            for j in range(n):
                dfs(i, j, [])
        return min_path

    return minPath(grid, k)

