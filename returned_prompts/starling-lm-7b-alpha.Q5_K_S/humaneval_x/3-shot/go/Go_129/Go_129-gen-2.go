    grid_size := len(grid)
    grid_size_squared := grid_size * grid_size
    grid_values := make([]int, grid_size_squared)
    for i := 0; i < grid_size; i++ {
        for j := 0; j < grid_size; j++ {
            grid_values[i*grid_size + j] = grid[i][j]
        }
    }
    grid_values_sorted := make([]int, grid_size_squared)
    copy(grid_values_sorted, grid_values)
    sort.Ints(grid_values_sorted)

    k_min_grid := 0
    for k_min_grid < k && grid_values_sorted[k_min_grid] <= k_min_grid + 1 {
        k_min_grid++
    }
    if k_min_grid == k {
        return []int{grid_values_sorted[0]}
    }

    minimum_path := []int{grid_values_sorted[k_min_grid]}
    while len(minimum_path) < k {
        if k_min_grid + 1 < grid_size_squared && grid_values_sorted[k_min_grid+1] <= k_min_grid + 2 {
            minimum_path = append(minimum_path, grid_values_sorted[k_min_grid+1])
            k_min_grid++
        }else{
            minimum_path = append(minimum_path, grid_values_sorted[k_min_grid])
            k_min_grid--
        }
    }
    return minimum_path
}



