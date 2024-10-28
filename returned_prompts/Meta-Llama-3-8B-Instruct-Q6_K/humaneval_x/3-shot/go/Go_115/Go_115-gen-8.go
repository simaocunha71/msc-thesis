    var result int
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[0]); j++ {
            result += grid[i][j]
        }
    }
    return result / capacity
}