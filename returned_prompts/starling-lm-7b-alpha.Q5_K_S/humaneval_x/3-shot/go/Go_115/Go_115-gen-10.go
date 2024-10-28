    result := 0
    n := len(grid)
    m := len(grid[0])
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if grid[i][j] == 1 {
                result += 1 + (grid[i][j] + capacity - 1) / capacity
            }
        }
    }
    return result
}



