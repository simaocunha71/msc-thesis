	for i := 1; i < k; i++ {
		for j := 0; j < len(grid)-i; j++ {
			for m := 0; m < len(grid)-i; m++ {
				if grid[j][m] < grid[j+i][m] {
					grid[j][m], grid[j+i][m] = grid[j+i][m], grid[j][m]
				}
			}
		}
	}
	return grid[0]
}

func main() {
	grid := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	k := 3
	fmt.Println(Minpath(grid, k))
}