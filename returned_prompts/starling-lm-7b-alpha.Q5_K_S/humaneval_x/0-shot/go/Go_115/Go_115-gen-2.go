    m, n := len(grid), len(grid[0])
    dp := make([][]int, m+1)
    for i := 0; i <= m; i++ {
        dp[i] = make([]int, n+1)
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                dp[i+1][j+1] = dp[i+1][j] + 1
            }
        }
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 0 {
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j+1]+1)
            }
        }
    }
    res := 0
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                cnt := dp[m][n] - dp[i][n] - dp[m][j] + dp[i][j]
                if cnt%capacity == 0 {
                    res++
                } else {
                    res += cnt/capacity + 1
                }
            }
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

func max(a, b int) int {
    if a < b {
        return b
    }
    return a
}

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                dp[i+1][j+1] = dp[i+1][j] + 1
            }
        }
    }
    for i := 0; i < m