    rows, cols := len(grid), len(grid[0])
    dist := make([][]int, rows)
    for i := range dist {
        dist[i] = make([]int, cols)
    }
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if i == 0 && j == 0 {
                dist[i][j] = grid[i][j]
            } else if i == 0 {
                dist[i][j] = dist[i][j-1] + grid[i][j]
            } else if j == 0 {
                dist[i][j] = dist[i-1][j] + grid[i][j]
            } else {
                dist[i][j] = min(dist[i-1][j], dist[i][j-1]) + grid[i][j]
            }
        }
    }
    min_path := make([]int, k)
    i, j := rows-1, cols-1
    for k > 0 {
        min_path[k-1] = grid[i][j]
        if i > 0 && j > 0 {
            if dist[i-1][j] < dist[i][j-1] {
                i -= 1
            } else {
                j -= 1
            }
        } else if i > 0 {
            i -= 1
        } else {
            j -= 1
        }
        k -= 1
    }
    return min_path
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}