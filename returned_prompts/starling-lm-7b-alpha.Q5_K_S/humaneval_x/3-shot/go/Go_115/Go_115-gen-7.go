    result := 0
    visited := make(map[int]bool)
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[0]); j++ {
            if grid[i][j] == 1 {
                result += 1 + dfs(grid, visited, i, j, capacity)
            }
        }
    }
    return result
}

func dfs(grid [][]int, visited map[int]bool, i, j, capacity int) int {
    if i < 0 || j < 0 || i >= len(grid) || j >= len(grid[0]) || grid[i][j] == 0 || visited[i*1000+j] {
        return 0
    }
    visited[i*1000+j] = true
    grid[i][j] = 0
    min := math.Min(float64(capacity), float64(grid[i][j]))
    grid[i][j] = int(min)
    result := 1
    result += max(grid, i-1, j, capacity)
    result += max(grid, i+1, j, capacity)
    result += max(grid, i, j-1, capacity)
    result += max(grid, i, j+1, capacity)
    return result
}

func max(grid [][]int, i, j, capacity int) int {
    if i < 0 || j < 0 || i >= len(grid) || j >= len(grid[0]) {
        return 0
    }
    return grid[i][j] / capacity
}



