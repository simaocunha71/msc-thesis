    def dfs(grid, k, current_path, current_index, visited):
        if k == 0:
            return current_path

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]:
                    continue
                if current_index < len(current_path):
                    if current_path[current_index] == grid[i][j]:
                        current_index += 1
                else:
                    current_path.append(grid[i][j])
                    visited[i][j] = True
                    result = dfs(grid, k-1, current_path, current_index, visited)
                    if result:
                        return result
                    visited[i][j] = False
                    current_path.pop()
        return None

    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    result = dfs(grid, k, [], 0, visited)
    return result
