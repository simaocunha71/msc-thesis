    // init variables
    var res, m, n int
    m = len(grid)
    n = len(grid[0])
    // init a queue
    var queue []int
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] != 0 {
                queue = append(queue, i*n+j)
            }
        }
    }
    // BFS
    for len(queue) != 0 {
        var i, j int
        i, j = queue[0] / n, queue[0] % n
        // queue[0] := queue[0] / n * n + queue[0] % n
        // queue[0] % n = i
        // queue[0] / n = j
        queue = queue[1:]
        for k := 0; k < 4; k++ {
            var nx, ny int
            nx = i + dir[k][0]
            ny = j + dir[k][1]
            if nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] <= capacity {
                res++
                grid[nx][ny] = 0
                queue = append(queue, nx*n+ny)
            }
        }
    }
    return res
}

// 