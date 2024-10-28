	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] == 1 {
				if k == 1 {
					return []int{1}
				}
				grid[i][j] = 0
				// up
				if i > 0 {
					grid[i-1][j]--
				}
				// down
				if i < len(grid)-1 {
					grid[i+1][j]--
				}
				// left
				if j > 0 {
					grid[i][j-1]--
				}
				// right
				if j < len(grid)-1 {
					grid[i][j+1]--
				}
				continue A
			}
		}
	}

	return []int{}
}

func Minpath2(grid [][]int, k int) []int {

	return []int{}
}

func Minpath3(grid [][]int, k int) []int {

	return []int{}
}

func main() {

	// grid := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	// k := 3

	// grid := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	// k := 9

	// grid := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	// k := 10

	grid := [][]int{{5, 9, 3}, {4, 1, 6}, {7, 8, 2}}
	k := 1

	// grid := [][]int{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}}
	// k := 4

	fmt.Println(Minpath(grid, k))
	fmt.Println(Minpath2(grid, k))
	fmt.Println(Minpath3(grid, k))
}

func Minpath4(grid [][]int, k int) []int {
	// find the min value in the grid
	min := grid[0][0]
	minX, minY := 