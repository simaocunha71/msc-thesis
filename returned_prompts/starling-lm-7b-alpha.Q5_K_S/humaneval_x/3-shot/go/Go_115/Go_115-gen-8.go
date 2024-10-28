    result := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            result += grid[i][j] / capacity
            grid[i][j] = grid[i][j] % capacity
        }
    }

    for i := 0; i < len(grid) - 1; i++ {
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] > 0 {
                grid[i+1][j] += grid[i][j]
                grid[i][j] = 0
            }
        }
    }
    for _, col := range grid[len(grid)-1] {
        if col > 0 {
            result += col
        }
    }
    return result
}



