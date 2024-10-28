	for {
		// Find the min element in the grid
		min := math.MaxInt32
		var r, c int
		for i, row := range grid {
			for j, v := range row {
				if v < min {
					min = v
					r = i
					c = j
				}
			}
		}
		grid[r][c] = math.MaxInt32

		if min > 0 {
			// If it is not the last step
			if k > 1 {
				// If the current min is greater than k
				if min > k {
					// Add the min to the list and continue
					return append([]int{min}, Minpath(grid, k-1)...)
				}
				// If the current min is less than k
				// Find the min element in the neighbor cells
				// and add the min to the list
				neighbor := make([]int, 0, 4)
				for i := r - 1; i <= r+1; i++ {
					for j := c - 1; j <= c+1; j++ {
						if i >= 0 && i < len(grid) && j >= 0 && j < len(grid[i]) {
							neighbor = append(neighbor, grid[i][j])
						}
					}
				}
				sort.Ints(neighbor)
				return append([]int{min}, Minpath(neighbor, k-1)...)
			}
			return []int{min}
		}

		// If it is the last step
		if k == 1 {
			return nil
		}

		// If it is not the last step