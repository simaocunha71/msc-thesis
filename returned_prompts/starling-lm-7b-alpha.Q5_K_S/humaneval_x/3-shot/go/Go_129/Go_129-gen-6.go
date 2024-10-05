    all_values := make(map[int]struct{}, 0)
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            all_values[grid[i][j]] = struct{}{}
        }
    }

    all_neighbors := make(map[int][]int, 0)
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            if i > 0 {
                all_neighbors[grid[i][j]] = append(all_neighbors[grid[i][j]], grid[i-1][j])
            }
            if i < len(grid)-1 {
                all_neighbors[grid[i][j]] = append(all_neighbors[grid[i][j]], grid[i+1][j])
            }
            if j > 0 {
                all_neighbors[grid[i][j]] = append(all_neighbors[grid[i][j]], grid[i][j-1])
            }
            if j < len(grid[i])-1 {
                all_neighbors[grid[i][j]] = append(all_neighbors[grid[i][j]], grid[i][j+1])
            }
        }
    }

    min_path := make([]int, 0)
    for i := 0; i < k; i++ {
        min_path = append(min_path, getMinNeighbor(min_path, all_values, all_neighbors))
    }
    return min_path
}

func getMinNeighbor(path []int, all_values map[int]struct{}, all_neighbors map[int][]int) int {
    min_value := math.MaxInt32
    for _, v := range path {
        if v < min_value {
            min_value = v
        }
    }
    min_neighbor := min_value