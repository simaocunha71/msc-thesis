    var total int
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            total += grid[i][j]
        }
    }
    var res int
    for total > 0 {
        res += total / capacity
        total %= capacity
    }
    return res
}