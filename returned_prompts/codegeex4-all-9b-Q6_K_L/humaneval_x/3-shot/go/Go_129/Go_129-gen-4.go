    result := make([]int, 0)

    // Find the minimum value in the grid
    min_value := grid[0][0]
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] < min_value {
                min_value = grid[i][j]
            }
        }
    }

    // Add the minimum value to the result
    result = append(result, min_value)

    // Find the next minimum value in the grid
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] == min_value {
                grid[i][j] = min_value + 1
            }
        }
    }

    // Repeat until we have found k values
    for i := 1; i < k; i++ {
        min_value = grid[0][0]
        for i := 0; i < len(grid); i++ {
            for j := 0; j < len(grid[i]); j++ {
                if grid[i][j] < min_value {
                    min_value = grid[i][j]
                }
            }
        }

        // Add the minimum value to the result
        result = append(result, min_value)

        // Find the next minimum value in the grid
        for i := 0; i < len(grid); i++ {
            for j := 0; j < len(grid[i]); j++ {
                if grid[i][j] == min_value {
                    grid[i][j] = min_value + 1
                }
            }
        }
    }

    return result
}

