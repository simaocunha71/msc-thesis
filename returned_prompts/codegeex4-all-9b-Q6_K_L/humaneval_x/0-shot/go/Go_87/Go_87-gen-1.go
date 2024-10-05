package main

import (
	"fmt"
	"sort"
)

func GetRow(lst [][]int, x int) [][2]int {
	var coords [][2]int

	for r, row := range lst {
		for c, val := range row {
			if val == x {
				coords = append(coords, [2]int{r, c})
			}
		}
	}

	sort.Slice(coords, func(i, j int) bool {
		if coords[i][0] == coords[j][0] {
			return coords[i][1] > coords[j][1]
		}
		return coords[i][0] < coords[j][0]
	})

	return coords
}

func main() {
	lst := [][]int{
		{1, 2, 3, 4, 5, 6},
		{1, 2, 3, 4, 1, 6},
		{1, 2, 3, 4, 5, 1},
	}

	fmt.Println(GetRow(lst, 1))
}

```