
}
*/

// Minpath finds the minimum path of length k in the grid.
func Minpath(grid [][]int, k int) []int {
	n := len(grid)
	type point struct {
		x, y, sum int
		path      []int
	}
	q := []point{{0, 0, grid[0][0], []int{grid[0][0]}}}
	minpath := []int{}
	for len(q) > 0 {
		p := q[0]
		q = q[1:]
		if len(p.path) == k {
			if len(minpath) == 0 || compare(p.path, minpath) < 0 {
				minpath = p.path
			}
			continue
		}
		for _, dir := range [][]int{{0, 1}, {1, 0}, {-1, 0}, {0, -1}} {
			x, y := p.x+dir[0], p.y+dir[1]
			if 0 <= x && x < n && 0 <= y && y < n {
				np := point{x, y, p.sum + grid[x][y], append([]int{}, append(p.path, grid[x][y])...)}
				q = append(q, np)
			}
		}
	}
	return minpath
}

func compare(a, b []int) int {
	for i := 0; i < len(a) && i < len(b); i++ {
		if a[i] < b[i] {
			return -1
		}
		if a[i] > b[i] {
			return 1
		}
	}
	if len(a) < len(b) {
		return -1
	}
	if len(a) > len(b) {
		return 1
	}
	return 0
}

/*
func main() {
	fmt.Println(Minpath([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, 3))