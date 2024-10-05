    result := make([]int, k)
    visited := make(map[int]bool)
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[0]); j++ {
            if grid[i][j] == 1 {
                result[0] = grid[i][j]
                visited[grid[i][j]] = true
            }
        }
    }
    return result
}



