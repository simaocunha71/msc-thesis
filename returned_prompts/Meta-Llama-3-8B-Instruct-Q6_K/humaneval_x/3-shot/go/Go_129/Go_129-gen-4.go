    rows, cols := len(grid), len(grid[0])
    visited := make([][]bool, rows)
    for i := range visited {
        visited[i] = make([]bool, cols)
    }
    minPath := make([]int, 0)

    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if dfs(grid, visited, i, j, k, &minPath) {
                return minPath
            }
        }
    }
    return minPath
}

func dfs(grid [][]int, visited [][]bool, i int, j int, k int, minPath *[]int) bool {
    rows, cols := len(grid), len(grid[0])
    (*minPath) = append((*minPath), grid[i][j])
    visited[i][j] = true
    if len(*minPath) == k {
        return true
    }
    directions := [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
    for _, dir := range directions {
        ni, nj := i + dir[0], j + dir[1]
        if ni >= 0 && ni < rows && nj >= 0 && nj < cols && !visited[ni][nj] {
            if dfs(grid, visited, ni, nj, k, minPath) {
                return true
            }
        }
    }
    (*minPath) = (*minPath)[:len(*minPath)-1]
    visited[i][j] = false
    return false
}