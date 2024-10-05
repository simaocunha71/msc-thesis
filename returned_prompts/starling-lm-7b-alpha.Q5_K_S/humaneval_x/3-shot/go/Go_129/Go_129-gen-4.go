    n := len(grid)
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            grid[i][j] += (i + j) * n
        }
    }

    min_path := make([]int, k)
    min_path[0] = 1
    min_dist := math.Inf(1)
    for len(min_path) < k {
        new_min_dist := math.Inf(1)
        for i := range min_path {
            for dx, dy := -1, 0, 0, 1; dx <= dy; dx, dy = dy, -1, 1 {
                x, y := min_path[i] % n, min_path[i] / n % n
                if dx != 0 || dy != 0 {
                    x += dx
                    y += dy
                }
                if x < 0 || y < 0 || x >= n || y >= n {
                    continue
                }
                if grid[x][y] < min_path[i] + 1 && grid[x][y] < new_min_dist {
                    new_min_dist = grid[x][y]
                    min_path[len(min_path):0] = make([]int, 0, k-len(min_path))
                    min_path[len(min_path)-1] = grid[x][y] - x * n - y
                }
            }
        }
        if new_min_dist == math.Inf(1) {
            break
        }
        min_dist = new_min_dist
    }
    return min_path
}

































































































