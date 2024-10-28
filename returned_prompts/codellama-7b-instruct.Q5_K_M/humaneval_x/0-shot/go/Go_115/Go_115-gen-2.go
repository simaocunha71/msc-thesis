    for i := range grid {
        for j := range grid[i] {
            if grid[i][j] == 1 {
                if j == len(grid[i])-1 {
                    continue A
                }
                if grid[i][j+1] == 1 {
                    continue A
                }
                return i
            }
        }
    }
    return -1
}
