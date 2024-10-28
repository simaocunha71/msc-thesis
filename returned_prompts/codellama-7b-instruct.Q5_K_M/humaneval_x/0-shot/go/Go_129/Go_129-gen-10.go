	for ; k > 0; k-- {
		for i := range grid {
			for j := range grid[i] {
				if grid[i][j] == 1 {
					continue A
				}
			}
		}
	}

	return nil
}
