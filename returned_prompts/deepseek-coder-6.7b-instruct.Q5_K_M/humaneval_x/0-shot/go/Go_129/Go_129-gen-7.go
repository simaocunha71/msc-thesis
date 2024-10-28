
}

*/

func MinPath(grid [][]int, k int) []int {
	n := len(grid)
	dx := []int{0, 0, -1, 1}
	dy := []int{-1, 1, 0, 0}
	res := make([]int, k)
	best := math.MaxInt64

	var dfs func(x, y, k int, path []int)
	dfs = func(x, y, k int, path []int) {
		if k == 0 {
			if len(path) < len(res) || (len(path) == len(res) && lexicoLess(path, res)) {
				res = append([]int(nil), path...)
			}
			return
		}
		for i := 0; i < 4; i++ {
			nx, ny := x+dx[i], y+dy[i]
			if nx >= 0 && nx < n && ny >= 0 && ny < n {
				dfs(nx, ny, k-1, append(path, grid[nx][ny]))
			}
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			dfs(i, j, k-1, []int{grid[i][j]})
		}
	}

	return res
}

func lexicoLess(a, b []int) bool {
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return a[i] < b[i]
		}
	}
	return false
}

func main() {
	grid := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	k := 3
	fmt.Println(MinPath(grid, k)) // [1, 2, 1]

	grid = [][]int{{5, 9, 3}, {