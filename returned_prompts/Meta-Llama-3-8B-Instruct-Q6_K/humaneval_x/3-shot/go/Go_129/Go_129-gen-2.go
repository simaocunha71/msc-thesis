    rows, cols := len(grid), len(grid[0])
    visited := make([][]bool, rows)
    for i := range visited {
        visited[i] = make([]bool, cols)
    }
    path := make([]int, 0)
    minPath := make([]int, 0)

    func dfs(r, c, k int) {
        if k == 0 {
            if len(path) < len(minPath) || (len(path) == len(minPath) && path < minPath) {
                minPath = path
            }
            return
        }
        for i := -1; i <= 1; i++ {
            for j := -1; j <= 1; j++ {
                nr, nc := r+i, c+j
                if nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc] {
                    path = append(path, grid[nr][nc])
                    visited[nr][nc] = true
                    dfs(nr, nc, k-1)
                    path = path[:len(path)-1]
                    visited[nr][nc] = false
                }
            }
        }
    }

    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            path = make([]int, 0)
            path = append(path, grid[i][j])
            visited[i][j] = true
            dfs(i, j, k)
            visited[i][j] = false
        }
    }
    return minPath
}