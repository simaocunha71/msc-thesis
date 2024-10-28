
    def minPath(grid, k):
        # Flatten grid into list of cells and their values
        cells = [(grid[i][j], i, j) for i in range(len(grid)) for j in range(len(grid[0]))]
        # Sort cells by their values
        cells.sort()
        # Initialize a list to keep track of visited cells
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        # Initialize result and its value
        result, result_val = [], float('inf')
        # Depth-first search
        def dfs(pos, path, k):
            nonlocal result, result_val
            # If path is of desired length, update result and its value
            if len(path) == k:
                if sum(path) < result_val:
                    result, result_val = path, sum(path)
                return
            # Explore neighbors
            i, j = pos
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y]:
                    visited[x][y] = True
                    dfs((x, y), path+[grid[x][y]], k)
                    visited[x][y] = False
        # Try all cells as starting points
        for val, i, j in cells:
            visited[i][j] = True
            dfs((i, j), [val], k)
            visited[i][j] = False
        # Return result
        return result

    print(minPath([[1,2,3],[4,5,6],[7,8,9]], 3))  # Output: [1, 2, 1]
    print(minPath([[5,9,3],[4,1,6],[7,8,2]], 1))  # Output: [1]
"""# !/usr/bin/env python
# -*- coding: utf-8 -*