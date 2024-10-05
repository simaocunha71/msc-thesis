
// This is a generic function to find the minimum path of a grid.
// It is a recursive function that tries to find the path with the minimum cost.
func minPath(grid [][]int, k int, currPos int, currCost int, currPath []int) []int {
	// We have found the minimum path.
	if currCost == k {
		return currPath
	}
	// We have exceeded the maximum length.
	if currCost > k {
		return nil
	}
	// Get all the neighboring cells.
	neighbors := [][]int{{0, -1}, {0, 1}, {-1, 0}, {1, 0}}
	minCost := math.MaxInt32
	minPath := []int{}
	for _, neighbor := range neighbors {
		pos := currPos + neighbor[0]*len(grid[0]) + neighbor[1]
		if pos < 0 || pos >= len(grid)*len(grid[0]) {
			continue
		}
		cost := currCost + 1
		path := append(currPath, grid[pos/len(grid[0])][pos%len(grid[0])])
		nextPath := minPath(grid, k, pos, cost, path)
		if nextPath != nil {
			if cost < minCost {
				minCost = cost
				minPath = nextPath
			} else if cost == minCost {
				if lexicographicallyLess(minPath, nextPath) {
					minPath = nextPath
				}
			}
		}
	}
	return minPath
}

// This function checks if a path is lexicographically less than another path.
// It does so by comparing each element at each index.
func lexicographicallyLess(path1, path2 []int) bool {
	for i := 0; i < len(path1); i++ {
		if path1[i] < path2[i] {
			return true
		} else if path1[i] > path