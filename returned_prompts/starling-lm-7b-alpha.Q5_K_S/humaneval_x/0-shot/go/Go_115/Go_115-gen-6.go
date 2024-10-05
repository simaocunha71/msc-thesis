    
    n := len(grid)
    m := len(grid[0])
    
    r := make([][]int, n)
    for i := 0; i < n; i++ {
        r[i] = make([]int, m)
        for j := 0; j < m; j++ {
            r[i][j] = grid[n-i-1][j]
        }
    }
    
    grid = r
    // for _, row := range grid {
    //     fmt.Println(row)
    // }
    
    cnt := 0
    for i := 0; i < n; i++ {
        cnt += grid[i][m-1] / capacity
        grid[i][m-1] = grid[i][m-1] % capacity
    }
    for i := m-2; i >= 0; i-- {
        for j := 0; j < n; j++ {
            if grid[j][i] == 0 {
                continue
            }
            grid[j][i] -= capacity
            if grid[j][i] < 0 {
                grid[j][i] += capacity
                cnt++
            }
        }
    }
    return cnt
}



// Time:  O(n * m)
// Space: O(n + m)


func MaxFill2(grid [][]int, capacity int) int {
    r := make([][]int, len(grid))
    for i := 0; i < len(r); i++ {
        r[i] = make([]int, len(grid[0]))
        for j := 0; j < len(grid[0]); j++ {
            r[i][j] = grid[len(grid)-i-1][j]
        }
    }
    grid = r
    cnt := 0
    for i := len(grid)-1; i >= 0; --i {
        cnt += grid[i][len(grid[0])-1] / capacity
        grid[i][len(grid[0])-1] %= capacity
    }
    for j := len(grid