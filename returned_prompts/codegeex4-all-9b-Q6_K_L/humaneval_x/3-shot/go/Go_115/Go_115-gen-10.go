    result := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            result += grid[i][j]
        }
    }
    return result / capacity
}



