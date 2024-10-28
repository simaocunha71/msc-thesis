
}


*/

package main

import (
	"fmt"
	"sort"
)

func minPath(grid [][]int, k int) []int {
	n := len(grid)
	dirs := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	type tuple struct{ cost, r, c, step int }
	heap := []tuple{{0, 0, 0, 0}}
	for len(heap) > 0 {
		sort.Slice(heap, func(i, j int) bool { return heap[i].cost < heap[j].cost })
		t := heap[0]
		heap = heap[1:]
		if t.step == k {
			return []int{grid[t.r][t.c]}
		}
		for _, d := range dirs {
			nr, nc := t.r+d[0], t.c+d[1]
			if 0 <= nr && nr < n && 0 <= nc && nc < n {
				heap = append(heap, tuple{t.cost + grid[nr][nc], nr, nc, t.step + 1})
			}
		}
	}
	return []int{}
}

func main() {
	fmt.Println(minPath([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, 3))
	fmt.Println(minPath([][]int{{5, 9, 3}, {4, 1, 6}, {7, 8, 2}}, 1))
}

// It's a path finding problem. We can use Dijkstra's algorithm to solve this problem.
// Dijkstra's algorithm is a shortest path algorithm in a graph that uses a priority queue.
// We can use a heap to store the cells that we need to visit next and the minimum path cost to each cell.
// The heap is sorted by the path cost of each cell, and we always visit