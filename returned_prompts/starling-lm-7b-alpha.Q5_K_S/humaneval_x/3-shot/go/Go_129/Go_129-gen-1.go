    result := make([]int, 0)
    visited := make([][]bool, len(grid))
    for i := 0; i < len(visited); i++ {
        visited[i] = make([]bool, len(grid[0]))
    }
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            result = append(result, grid[i][j])
            visited[i][j] = true
        }
    }

    for i := 0; i < k; i++ {
        min_index := -1
        min_value := math.MaxInt32
        for j := 0; j < len(grid); j++ {
            for l := 0; l < len(grid[j]); l++ {
                if !visited[j][l] {
                    if grid[j][l] < min_value {
                        min_index = j * len(grid[0]) + l
                        min_value = grid[j][l]
                    }
                }
            }
        }
        result[i] = grid[min_index / len(grid[0])][min_index % len(grid[0])]
        visited[min_index / len(grid[0])][min_index % len(grid[0])] = true
    }
    return result
}












































































































































































