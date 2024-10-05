    rows, cols := len(grid), len(grid[0])
    dp := make([][]int, rows)
    for i := range dp {
        dp[i] = make([]int, cols)
    }
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            dp[i][j] = grid[i][j]
        }
    }
    for k := 1; k <= k; k++ {
        for i := 0; i < rows; i++ {
            for j := 0; j < cols; j++ {
                if i > 0 {
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
                }
                if j > 0 {
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
                }
                if i < rows - 1 {
                    dp[i][j] = min(dp[i][j], dp[i+1][j])
                }
                if j < cols - 1 {
                    dp[i][j] = min(dp[i][j], dp[i][j+1])
                }
            }
        }
    }
    res := make([]int, k)
    i, j := 0, 0
    for k := k; k > 0; k-- {
        res[k-1] = dp[i][j]
        if i > 0 {
            i--
        } else if j > 0 {
            j--
        } else {
            i++
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