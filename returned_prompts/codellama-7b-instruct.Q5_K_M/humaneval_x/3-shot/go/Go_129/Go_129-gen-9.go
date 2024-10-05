    // Get the size of the grid
    rows := len(grid)
    cols := len(grid[0])

    // If k is greater than the number of cells, there is no path
    if k > rows * cols {
        return nil
    }

    // Create a list of all the possible paths that go through the grid
    paths := make([][]int, 0)
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            path := []int{grid[i][j]}
            if i > 0 {
                path = append(path, grid[i-1][j])
            }
            if j > 0 {
                path = append(path, grid[i][j-1])
            }
            paths = append(paths, path)
        }
    }

    // Sort the paths by the value of the first cell
    sort.Slice(paths, func(i, j int) bool {
        return paths[i][0] < paths[j][0]
    })

    // Get the shortest path
    shortest := paths[0]
    for _, path := range paths {
        if len(path) == k {
            return path
        }
        if len(path) < len(shortest) {
            shortest = path
        }
    }

    // If the shortest path is not the same length as k, return nil
    if len(shortest) != k {
        return nil
    }

    // Return the shortest path
    return shortest
}



