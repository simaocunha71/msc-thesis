    n := len(grid)
    min := math.MaxInt32
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if i < n-1 && grid[i][j] < min {
                min = grid[i][j]
            }
            if j < n-1 && grid[i][j] < min {
                min = grid[i][j]
            }
        }
    }
    return []int{min}
}



