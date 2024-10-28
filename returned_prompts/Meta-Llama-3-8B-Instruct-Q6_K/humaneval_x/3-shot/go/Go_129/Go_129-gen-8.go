    rows, cols := len(grid), len(grid[0])
    visited := make([][]bool, rows)
    for i := 0; i < rows; i++ {
        visited[i] = make([]bool, cols)
    }
    path := make([]int, 0)
    directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
    minPath := make([]int, 0)
    var dfs func(int, int, int, []int)
    dfs = func(i, j, k, path []int) {
        path = append(path, grid[i][j])
        if k == 0 {
            if len(minPath) == 0 || path < minPath {
                minPath = path
            }
        } else {
            for _, direction := range directions {
                ni, nj := i + direction[0], j + direction[1]
                if ni >= 0 && ni < rows && nj >= 0 && nj < cols && !visited[ni][nj] {
                    visited[ni][nj] = true
                    dfs(ni, nj, k-1, path)
                    visited[ni][nj] = false
                }
            }
        }
    }
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            visited[i][j] = true
            dfs(i, j, k, make([]int, 0))
            visited[i][j] = false
        }
    }
    return minPath
} 