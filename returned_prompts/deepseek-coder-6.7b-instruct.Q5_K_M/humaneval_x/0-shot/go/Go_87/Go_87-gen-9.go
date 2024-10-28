    var res [][2]int
    for i, row := range lst {
        for j, val := range row {
            if val == x {
                res = append(res, [2]int{i, j})
            }
        }
    }

    sort.Slice(res, func(i, j int) bool {
        if res[i][0] == res[j][0] {
            return res[i][1] > res[j][1]
        } 
        return res[i][0] < res[j][0]
    })

    return res
}

*/

package main

import (
	"fmt"
	"sort"
)

func GetRow(lst [][]int, x int) [][2]int {
	var res [][2]int
	for i, row := range lst {
		for j, val := range row {
			if val == x {
				res = append(res, [2]int{i, j})
			}
		}
	}

	sort.Slice(res, func(i, j int) bool {
		if res[i][0] == res[j][0] {
			return res[i][1] > res[j][1]
		}
		return res[i][0] < res[j][0]
	})

	return res
}

func main() {
	lst := [][]int{{1, 2, 3, 4, 5, 6}, {1, 2, 3, 4, 1, 6}, {1, 2, 3, 4, 5, 1}}
	x := 1
	res := GetRow(lst, x)
	fmt.Println(res)
}
package main

import (
	"fmt"
	"strings"
)

// You are given an integer array nums. You are initially positioned at the array's first index,
// and each element in the array represents your maximum jump length at that position.
// Return true if you can reach the last index, or false otherwise.
//
