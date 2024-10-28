    n := len(grid)
    directions := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
    visited := make([][]bool, n)
    for i := 0; i < n; i++ {
        visited[i] = make([]bool, n)
    }
    result := make([]int, 0)

    var dfs func(int, int, int)
    dfs = func(x, y, pathLength int) {
        if pathLength == k {
            result = append(result, grid[x][y])
            return
        }

        visited[x][y] = true
        for _, dir := range directions {
            newX, newY := x+dir[0], y+dir[1]
            if newX >= 0 && newX < n && newY >= 0 && newY < n && !visited[newX][newY] {
                dfs(newX, newY, pathLength+1)
            }
        }
        visited[x][y] = false
    }

    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            dfs(i, j, 0)
        }
    }

    sort.Ints(result)
    return result
}