	for {
		// 1. find the cell with min value
		min := math.MaxInt64
		var i, j int
		for i = 0; i < len(grid); i++ {
			for j = 0; j < len(grid[0]); j++ {
				if grid[i][j] < min {
					min = grid[i][j]
				}
			}
		}
		if min == math.MaxInt64 {
			break A
		}
		// 2. find all cells with min value
		cells := [][]int{}
		for i = 0; i < len(grid); i++ {
			for j = 0; j < len(grid[0]); j++ {
				if grid[i][j] == min {
					cells = append(cells, []int{i, j})
				}
			}
		}
		// 3. find the path
		path := []int{}
		for len(cells) > 0 {
			// find the min cell
			min_i, min_j, min := -1, -1, math.MaxInt64
			for i := 0; i < len(cells); i++ {
				if cells[i][0] < min_i {
					min_i, min_j, min = cells[i][0], cells[i][1], grid[cells[i][0]][cells[i][1]]
				} else if cells[i][0] == min_i && cells[i][1] < min_j {
					min_j, min = cells[i][1], grid[cells[i][0]][cells[i][1]]
				}
			}
			// append min cell to path
			path = append(path, min)
			// remove min cell from cells
	