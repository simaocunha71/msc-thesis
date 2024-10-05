	for i := 0; i < k; i++ {
		for j := 0; j < len(grid); j++ {
			if i == 0 {
				grid[j][0] += j
			} else {
				grid[j][0] += min(grid[j][i-1], grid[j-1][i-1])
			}
			grid[j][0] = grid[j][0] % (len(grid) * len(grid))
			grid[j][0] += grid[j][i]
			grid[j][0] = grid[j][0] % (len(grid) * len(grid))
		}
	}

	for i := 0; i < len(grid); i++ {
		fmt.Println(grid[i][0])
	}

	return nil
}

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func min2(a, b, c int) int {
	if a < b {
		if a < c {
			return a
		} else {
			return c
		}
	} else {
		if b < c {
			return b
		} else {
			return c
		}
	}
}

func main() {

	Minpath([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, 3)
	Minpath([][]int{{5, 9, 3}, {4, 1, 6}, {7, 8, 2}}, 1)

}

// 1 2 3
// 4 5 6
// 7 8 9

// 1 2 3 4 5 6 7 8 9
// 2 3 4 5 6 7 8 9 10
// 3 4 5 6 7 8 9 10 11

// 1 2 3 4 5 6 7 8 9
// 4 5 6 7 8 9 10 11 12
// 7 8 9 10 11 12 13 14 15

// 1 2 3 4 5 6 7 8 9
// 9 10 11 12 13