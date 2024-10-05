    result := 0
    for i := 0; i < len(grid); i++ {
        var current_capacity int = capacity
        for j := 0; j < len(grid[i]); j++ {
            if current_capacity > 0 && grid[i][j] == 1{
                current_capacity--
            }

            if current_capacity == 0{
                break
            }
        }

        if current_capacity != 0{
            result += capacity - current_capacity
        }
    }
    return result
}



