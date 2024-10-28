    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[0]); j++ {
            if grid[i][j] == 0 {
                continue
            }
            for k := 0; k < len(grid[0]); k++ {
                if grid[i][k] == 0 || grid[i][k] == grid[i][j] {
                    continue
                }
                if grid[i][k] != grid[i][j] {
                    grid[i][k] = grid[i][j]
                    if grid[i][k] == capacity {
                        goto A
                    }
                }
            }
        }
    }
    return 0
}
