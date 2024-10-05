    total := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[0]); j++ {
            total += grid[i][j]
        }
    }
    return math.Ceil(float64(total) / float64(capacity))
}

