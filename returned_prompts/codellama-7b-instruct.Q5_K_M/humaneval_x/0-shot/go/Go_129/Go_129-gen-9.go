	for i := 1; i < k; i++ {
		for j := range grid {
			for l := range grid[j] {
				if grid[j][l] == i {
					continue A
				}
			}
		}
		return nil
	}

	return nil
}
