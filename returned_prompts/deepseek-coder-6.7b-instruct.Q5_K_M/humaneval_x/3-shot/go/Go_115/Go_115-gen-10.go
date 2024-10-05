    total_water :=0
    for i:=0; i<len(grid); i++ {
        for j:=0; j<len(grid[i]); j++ {
            total_water += grid[i][j]
        }
    }
    return int(math.Ceil(float64(total_water)/float64(capacity)))
}



