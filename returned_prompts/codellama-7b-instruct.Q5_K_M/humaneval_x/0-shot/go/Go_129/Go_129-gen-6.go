
	for i, g := range grid {
		for j, v := range g {
			if v == 1 {
				// found start
				start := i*len(g) + j
				if k == 1 {
					// only one step, no need to search
					return []int{v}
				}
				// search
				var visited [][2]int
				search(&visited, start, k)
				break A
			}
		}
	}

	// find shortest path
	var shortest int = math.MaxInt32
	var path []int
	for _, v := range visited {
		if v[1] < shortest {
			shortest = v[1]
			path = v[0]
		}
	}

	return path
}

func search(visited *[][2]int, start int, k int) {

	if k == 0 {
		return
	}

	var r []int
	var c []int
	var i int
	var j int

	// get all neighbors
	for i = start / len(*visited); i < start/len(*visited)+2; i++ {
		for j = start%len(*visited); j < start%len(*visited)+2; j++ {
			if i < len(*visited) && j < len(*visited) && i >= 0 && j >= 0 {
				r = append(r, i)
				c = append(c, j)
			}
		}
	}

	// check if neighbor is visited
	for i, r := range r {
		for j, c := range c {
			if visited[r][c] == 0 {
				// not visited
				visited[r][c] = 1
				// search
				search(visited, r*len(*