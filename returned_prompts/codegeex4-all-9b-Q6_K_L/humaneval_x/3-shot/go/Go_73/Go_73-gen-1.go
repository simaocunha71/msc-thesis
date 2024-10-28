    n := len(arr)
    dp := make([][]int, n)
    for i := range dp {
        dp[i] = make([]int, n)
    }
    dp[0][0] = 0
    for i := 1; i < n; i++ {
        dp[i][i] = 1
    }

    for i := n - 1; i >= 0; i-- {
        for j := i + 1; j < n; j++ {
            if arr[i] == arr[j] {
                dp[i][j] = dp[i+1][j-1]
            } else {
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
            }
        }
    }
    return dp[0][n-1]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}



