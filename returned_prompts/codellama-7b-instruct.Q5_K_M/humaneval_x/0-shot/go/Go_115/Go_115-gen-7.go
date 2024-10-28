    for i := len(grid) - 1; i >= 0; i-- {
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] == 0 {
                continue
            }
            if j == 0 || grid[i][j-1] == 0 {
                continue
            }
            if j == len(grid[i])-1 || grid[i][j+1] == 0 {
                continue
            }

            grid[i][j] = grid[i][j-1] + grid[i][j+1]
            if grid[i][j] > capacity {
                continue A
            }
        }
    }

    count := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] == 0 {
                continue
            }
            count++
        }
    }
    return count
}
