	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				goto B
			}
		}
	}
	return nil

B:
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				grid[i][j] = 1
			} else {
				grid[i][j] = 0
			}
		}
	}
	var ans []int
	for i := 0; i < k; i++ {
		ans = append(ans, grid[0][0])
		for j := 0; j < len(grid[0]); j++ {
			grid[0][j] += grid[0][j]
		}
		for i := 1; i < len(grid); i++ {
			for j := 0; j < len(grid[0]); j++ {
				grid[i][j] += grid[i-1][j]
			}
		}
	}
	return ans
}
