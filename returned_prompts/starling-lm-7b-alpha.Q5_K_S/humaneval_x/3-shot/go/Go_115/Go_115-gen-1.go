    rows := len(grid)
    cols := len(grid[0])
    result := 0
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if grid[i][j] == 0 {
                continue
            }
            if grid[i][j] > capacity {
                grid[i][j] = capacity
                result += 1
            }
            grid[i][j] -= 1
            for k := j + 1; k < cols; k++ {
                if grid[i][k] == 0 {
                    continue
                }
                if grid[i][k] > capacity {
                    grid[i][k] = capacity
                    result += 1
                }
                grid[i][k] -= 1
            }
        }
    }
    return result
}



