
}

*/

package main

import (
	"fmt"
	"sort"
)

type cell struct {
	i, j, val int
}

type path struct {
	vals []int
}

func minPath(grid [][]int, k int) []int {
	n := len(grid)
	cells := make([]cell, 0, n*n)
	for i := range grid {
		for j := range grid[i] {
			cells = append(cells, cell{i, j, grid[i][j]})
		}
	}
	sort.Slice(cells, func(i, j int) bool {
		return cells[i].val < cells[j].val
	})

	paths := make([]path, n*n+1)
	for _, cell := range cells {
		for l := range paths {
			if l == 0 || l == cell.val {
				newPath := make([]int, len(paths[l-1].vals))
				copy(newPath, paths[l-1].vals)
				newPath = append(newPath, cell.val)
				paths[l] = path{newPath}
			} else if l > cell.val && len(paths[l-cell.val].vals) > 0 {
				newPath := make([]int, len(paths[l-cell.val].vals))
				copy(newPath, paths[l-cell.val].vals)
				newPath = append(newPath, cell.val)
				if len(paths[l].vals) == 0 || less(newPath, paths[l].vals) {
					paths[l] = path{newPath}
				}
			}
		}
	}
	return paths[k].vals
}

func less(a, b []int) bool {
	for i := range a {
		if a[i] != b[i] {
			return a[i] < b[i]
		}
	}
	return false
}

func main() {
	fmt.Println(minPath([][]int