    var result [][2]int

    for i, row := range lst {
        for j, value := range row {
            if value == x {
                result = append(result, [2]int{i, j})
            }
        }
    }

    sort.Slice(result, func(i, j int) bool {
        if result[i][0] == result[j][0] {
            return result[i][1] > result[j][1]
        }
        return result[i][0] < result[j][0]
    })

    return result
}

*/

package main

import (
	"fmt"
	"sort"
)

func GetRow(lst [][]int, x int) [][2]int {
	var result [][2]int

	for i, row := range lst {
		for j, value := range row {
			if value == x {
				result = append(result, [2]int{i, j})
			}
		}
	}

	sort.Slice(result, func(i, j int) bool {
		if result[i][0] == result[j][0] {
			return result[i][1] > result[j][1]
		}
		return result[i][0] < result[j][0]
	})

	return result
}

func main() {
	lst := [][]int{
		{1, 2, 3, 4, 5, 6},
		{1, 2, 3, 4, 1, 6},
		{1, 2, 3, 4, 5, 1},
	}
	fmt.Println(GetRow(lst, 1)) // [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

	lst = [][]int{}
	fmt.Println(GetRow(lst, 1)) // []

	lst = [][]int{
		{},
		{1},
		{1, 