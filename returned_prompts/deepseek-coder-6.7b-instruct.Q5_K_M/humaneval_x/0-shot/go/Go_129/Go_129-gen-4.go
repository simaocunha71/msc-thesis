
}
*/

import (
	"container/heap"
	"sort"
)

type Cell struct {
	val  int
	dist int
	path []int
}

type CellHeap []*Cell

func (h CellHeap) Len() int           { return len(h) }
func (h CellHeap) Less(i, j int) bool { return h[i].val < h[j].val }
func (h CellHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *CellHeap) Push(x interface{}) {
	*h = append(*h, x.(*Cell))
}

func (h *CellHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func minPath(grid [][]int, k int) []int {
	n := len(grid)
	dx := []int{0, 0, -1, 1}
	dy := []int{-1, 1, 0, 0}

	h := &CellHeap{&Cell{val: grid[0][0], dist: 0, path: []int{grid[0][0]}}}
	heap.Init(h)

	visited := make([][]bool, n)
	for i := range visited {
		visited[i] = make([]bool, n)
	}
	visited[0][0] = true

	for h.Len() > 0 {
		cell := heap.Pop(h).(*Cell)
		if cell.dist == k-1 {
			return cell.path
		}

		for i := 0; i < 4; i++ {
			nx, ny := cell.x+dx[i], cell.y+dy[i]
			if nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny