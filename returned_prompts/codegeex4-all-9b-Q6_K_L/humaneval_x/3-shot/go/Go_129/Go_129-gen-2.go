    result := make([]int, 0)
    visited := make([][]bool, len(grid))
    for i := range visited {
        visited[i] = make([]bool, len(grid))
    }
    for i := range grid {
        for j := range grid[i] {
            if MinpathHelper(grid, visited, i, j, k, 0) {
                result = append(result, grid[i][j])
            }
        }
    }
    return result
}

func MinpathHelper(grid [][]int, visited [][]bool, i int, j int, k int, current int) bool {
    if i < 0 || j < 0 || i >= len(grid) || j >= len(grid) || visited[i][j] || current >= k {
        return false
    }
    if current == k-1 {
        return true
    }
    visited[i][j] = true
    result := false
    result = result || MinpathHelper(grid, visited, i+1, j, k, current+1)
    result = result || MinpathHelper(grid, visited, i-1, j, k, current+1)
    result = result || MinpathHelper(grid, visited, i, j+1, k, current+1)
    result = result || MinpathHelper(grid, visited, i, j-1, k, current+1)
    visited[i][j] = false
    return result
}



