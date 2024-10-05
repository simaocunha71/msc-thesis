    rows, cols := len(grid), len(grid[0])
    visited := make([][]bool, rows)
    for i := range rows {
        visited[i] = make([]bool, cols)
    }
    res := 0
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if grid[i][j] == 1 {
                dfs(grid, visited, i, j, capacity, &res)
            }
        }
    }
    return res
}

func dfs(grid [][]int, visited [][]bool, i int, j int, capacity int, res *int) {
    if i < 0 || i >= len(grid) || j < 0 || j >= len(grid[0]) || visited[i][j] {
        return
    }
    visited[i][j] = true
    for k := 1; k <= capacity; k++ {
        if i+k < len(grid) && grid[i+k][j] == 1 {
            dfs(grid, visited, i+k, j, capacity, res)
        }
        if j+k < len(grid[0]) && grid[i][j+k] == 1 {
            dfs(grid, visited, i, j+k, capacity, res)
        }
    }
    (*res)++
}