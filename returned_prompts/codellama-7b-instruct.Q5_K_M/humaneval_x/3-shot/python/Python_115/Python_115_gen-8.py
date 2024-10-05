    def dfs(i, j, visited, bucket_capacity, grid, result):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == 0 or visited[i][j]:
            return

        visited[i][j] = True
        current_capacity = min(bucket_capacity, grid[i][j])
        grid[i][j] -= current_capacity
        result += 1

        dfs(i - 1, j, visited, bucket_capacity - current_capacity, grid, result)
        dfs(i, j - 1, visited, bucket_capacity - current_capacity, grid, result)
        dfs(i + 1, j, visited, bucket_capacity - current_capacity, grid, result)
        dfs(i, j + 1, visited, bucket_capacity - current_capacity, grid, result)

    def get_max_well_length(grid):
        return max([len(grid[0]), len(grid)])

    def get_result(grid, bucket_capacity):
        result = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        well_length = get_max_well_length(grid)

        for i in range(well_length):
            for j in range(well_length):
                dfs(i, j, visited, bucket_capacity, grid, result)

        return result

    return get_result(grid, capacity)


