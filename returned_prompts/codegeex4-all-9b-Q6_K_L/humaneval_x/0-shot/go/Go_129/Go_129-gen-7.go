	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid); j++ {
			//fmt.Printf("grid[%d][%d] = %d\n", i, j, grid[i][j])
			path := make([]int, 0)
			path = append(path, grid[i][j])
			//fmt.Printf("path = %v\n", path)
			if path[0] == 1 {
				if k == 1 {
					return path
				}
				//fmt.Printf("k = %d\n", k)
				for kk := 1; kk < k; kk++ {
					//fmt.Printf("kk = %d\n", kk)
					if i > 0 && j > 0 {
						path = append(path, grid[i-1][j-1])
						//fmt.Printf("path = %v\n", path)
						if path[len(path)-1] == k {
							return path
						}
					}
					if i > 0 {
						path = append(path, grid[i-1][j])
						//fmt.Printf("path = %v\n", path)
						if path[len(path)-1] == k {
							return path
						}
					}
					if i > 0 && j < len(grid)-1 {
						path = append(path, grid[i-1][j+1])
						//fmt.Printf("path = %v\n", path)
						if path[len(path)-1] == k {
							return path
						}
					}
					if j > 0 {
						path = append(path, grid[i][j-1])
						//fmt.Printf("path = %v\n", path)
						if path[len(path)-1] == k {
							return path
						}
					}
					if j < len(grid)-1 {
						path = append(path, grid[i][j+1])
						//fmt.Printf("path = %v\n", path)
						if path[len(path)-1] == k {
							return path
						}
					}
					if i < len(grid)-1 && j > 0 {
						path = append(path, grid[i+1][j-1])
						//fmt.Printf("path = %v\n", path)
						if path[len(path)-1] == k {
							return path
						}
				