    // 1. Initialize variables
    n := len(grid)
    direction := [][]int{{-1, 0}, {0, -1}, {1, 0}, {0, 1}}
    visited := make([][]bool, n)
    for i := range visited {
        visited[i] = make([]bool, n)
    }
    res := make([]int, k)
    minVal := math.MaxInt32

    // 2. Define dfs function to find the minimum path
    var dfs func(int, int, int, int)
    dfs = func(x, y, steps, sum int) {
        if steps == k {
            if sum < minVal {
                minVal = sum
                copy(res, grid[x][y:y+k])
            }
            return
        }
        for _, d := range direction {
            nx, ny := x+d[0], y+d[1]
            if nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny] {
                visited[nx][ny] = true
                dfs(nx, ny, steps+1, sum+grid[nx][ny])
                visited[nx][ny] = false
            }
        }
    }

    // 3. Start dfs from each cell
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            visited[i][j] = true
            dfs(i, j, 1, grid[i][j])
            visited[i][j] = false
        }
    }

    return res
}



