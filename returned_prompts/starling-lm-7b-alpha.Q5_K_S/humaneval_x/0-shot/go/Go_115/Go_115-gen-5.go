    var (
        m = len(grid)
        n = len(grid[0])
    )
    var (
        dp = make([][]int, m)
        tmp = make([][]int, m)
    )
    for i := 0; i < m; i++ {
        dp[i] = make([]int, n)
        tmp[i] = make([]int, n)
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                dp[i][j] = 1
                tmp[i][j] = 1
            }
        }
    }

    for k := 0; k < capacity; k++ {
        for i := 0; i < m; i++ {
            for j := 0; j < n; j++ {
                if grid[i][j] == 0 {
                    continue
                }

                if i > 0 {
                    tmp[i][j] += tmp[i-1][j]
                }
                if j > 0 {
                    tmp[i][j] += tmp[i][j-1]
                }
                if i > 0 && j > 0 {
                    tmp[i][j] -= tmp[i-1][j-1]
                }

                if tmp[i][j] == 0 {
                    dp[i][j] = k + 1
                } else {
                    dp[i][j] = k + 1 + tmp[i][j] % capacity
                }

                tmp[i][j] = 0
            }
        }
    }

    return dp[m-1][n-1]
}




































































