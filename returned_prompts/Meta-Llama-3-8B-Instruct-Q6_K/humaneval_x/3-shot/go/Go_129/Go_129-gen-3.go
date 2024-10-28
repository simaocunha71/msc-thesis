    rows, cols := len(grid), len(grid[0])
    dp := make([][]int, rows)
    for i := 0; i < rows; i++ {
        dp[i] = make([]int, cols)
    }
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if i == 0 && j == 0 {
                dp[i][j] = grid[i][j]
            } else if i == 0 {
                dp[i][j] = dp[i][j-1] + grid[i][j]
            } else if j == 0 {
                dp[i][j] = dp[i-1][j] + grid[i][j]
            } else {
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            }
        }
    }
    res := make([]int, k)
    i, j := rows-1, cols-1
    for k := k; k > 0; k-- {
        res[k-1] = dp[i][j]
        if i > 0 {
            i--
        } else {
            j--
        }
    }
    return res
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
}