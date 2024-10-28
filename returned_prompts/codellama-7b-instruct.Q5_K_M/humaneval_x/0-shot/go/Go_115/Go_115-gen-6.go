	for {
		row_max := 0
		for i := 0; i < len(grid); i++ {
			row_max = max(row_max, grid[i][0])
		}
		if row_max == 0 {
			break
		}

		for i := 0; i < len(grid); i++ {
			if grid[i][0] > 0 {
				if grid[i][0] > capacity {
					grid[i][0] -= capacity
				} else {
					grid[i][0] = 0
				}
			}
		}
	}

	row_max = 0
	for i := 0; i < len(grid); i++ {
		row_max = max(row_max, grid[i][0])
	}

	return row_max
}

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}
