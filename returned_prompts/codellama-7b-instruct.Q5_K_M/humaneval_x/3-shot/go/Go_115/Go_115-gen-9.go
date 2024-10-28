    var result int
    for i := 0; i < len(grid); i++ {
        if grid[i][0] == 1 {
            result += capacity
        }
    }
    return result
}



