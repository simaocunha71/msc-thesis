
}

*/

package main

import (
	"fmt"
	"sort"
)

type Cell struct {
	val    int
	row, col int
}

type Path struct {
	values []int
	grid   [][]int
}

func (p *Path) Len() int {
	return len(p.values)
}

func (p *Path) Less(i, j int) bool {
	if p.values[i] < p.values[j] {
		return true
	} else if p.values[i] > p.values[j] {
		return false
	} else {
		pi := p.values[i]
		pj := p.values[j]

		ci := p.values[i]
		cj := p.values[j]

		if pi < pj {
			return true
		} else if pi > pj {
			return false
		} else {
			if ci < cj {
				return true
			} else {
				return false
			}
		}
	}
}

func (p *Path) Swap(i, j int) {
	p.values[i], p.values[j] = p.values[j], p.values[i]
}

func minPath(grid [][]int, k int) []int {
	N := len(grid)

	cells := make([]Cell, 0, N*N)

	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			cells = append(cells, Cell{grid[i][j], i, j})
		}
	}

	sort.Slice(cells, func(i, j int) bool {
		return cells[i].val < cells[j].val
	})

	path := Path{make([]int, 0, k), grid}

	dirs := [][]int{
		{-1, 0},
		{0, -1},
		{0, 1},
		{1, 0},
	}

	