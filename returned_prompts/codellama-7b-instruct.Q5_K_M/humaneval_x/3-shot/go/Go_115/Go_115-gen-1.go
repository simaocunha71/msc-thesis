    rows := len(grid)
    cols := len(grid[0])
    max_fill := 0
    for i := 0; i < rows; i++ {
        current_fill := 0
        for j := 0; j < cols; j++ {
            if grid[i][j] == 1{
                current_fill += 1
            }

            if current_fill > capacity{
                break
            }

            if j == cols - 1{
                max_fill = int(math.Max(float64(max_fill), float64(current_fill)))
            }
        }
    }
    return max_fill
}



