	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] == 1 {
				return Minpath(grid, k, i, j)
			}
		}
	}
	return nil
}

func Minpath(grid [][]int, k int, i int, j int) []int {

	if i < 0 || j < 0 {
		return nil
	}
	if i > len(grid)-1 || j > len(grid)-1 {
		return nil
	}

	if k == 1 {
		return []int{grid[i][j]}
	}

	if k == 2 {
		return []int{grid[i][j], grid[i][j]}
	}

	if k == 3 {
		return []int{grid[i][j], grid[i][j], grid[i][j]}
	}

	if k == 4 {
		return []int{grid[i][j], grid[i][j], grid[i][j], grid[i][j]}
	}

	if k == 5 {
		return []int{grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j]}
	}

	if k == 6 {
		return []int{grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j]}
	}

	if k == 7 {
		return []int{grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j]}
	}

	if k == 8 {
		return []int{grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j]}
	}

	if k == 9 {
		return []int{grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j]}
	}

	if k == 10 {
		return []int{grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i][j], grid[i