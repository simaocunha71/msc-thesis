    // Get the size of the grid
    var rows int = len(grid)
    var cols int = len(grid[0])

    // Create a matrix to store the minimum path for each cell
    min_path := make([][]int, rows)
    for i := 0; i < rows; i++ {
        min_path[i] = make([]int, cols)
    }

    // Initialize the first row and column of the matrix
    for i := 0; i < rows; i++ {
        min_path[i][0] = i
    }
    for j := 0; j < cols; j++ {
        min_path[0][j] = j
    }

    // Fill the matrix
    for i := 1; i < rows; i++ {
        for j := 1; j < cols; j++ {
            // Find the minimum path from the top and left cell
            min_path[i][j] = min(min_path[i-1][j], min_path[i][j-1])
            // Check if the current cell is smaller than the minimum path
            if grid[i][j] < min_path[i][j] {
                min_path[i][j] = grid[i][j]
            }
        }
    }

    // Get the kth smallest element
    kth_smallest := min_path[rows-1][cols-1]
    for i := 0; i < k-1; i++ {
        kth_smallest = min(kth_smallest, min_path[i][cols-1])
    }

    // Return the path
    result := []int{}
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if min_path[i][j] == kth_smallest {
                result = append(result, grid[i][j])
                break
            }
        }
    }
    return result
}



