    result := 0
    water := 0

    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            water += grid[i][j]
        }
    }

    for {
        water -= capacity
        if water < 0 {
            return result
        }
        result++
    }
}



