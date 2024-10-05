    var min_values []int
    var min_values_len int

    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[0]); j++ {
            if grid[i][j] < k {
                min_values = append(min_values, grid[i][j])
                min_values_len++
            }
        }
    }
    return min_values
}



