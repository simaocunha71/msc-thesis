
    // Your code goes here

    return 0
}
*/

package main

import (
	"fmt"
)

func MaxFill(grid [][]int, capacity int) int {
	count := 0
	buckets := 0
	for _, row := range grid {
		for _, well := range row {
			if well == 1 {
				buckets++
			}
		}
	}

	for buckets > 0 {
		count++
		buckets -= capacity
	}
	return count
}

func main() {
	fmt.Println(MaxFill([][]int{{0, 0, 1, 0}, {0, 1, 0, 0}, {1, 1, 1, 1}}, 1)) // Output: 6
	fmt.Println(MaxFill([][]int{{0, 0, 1, 1}, {0, 0, 0, 0}, {1, 1, 1, 1}, {0, 1, 1, 1}}, 2)) // Output: 5
	fmt.Println(MaxFill([][]int{{0, 0, 0}, {0, 0, 0}}, 5)) // Output: 0
}

// 0 0 1 0
// 0 1 0 0
// 1 1 1 1

// 0 0 1 1
// 0 0 0 0
// 1 1 1 1
// 0 1 1 1

// 0 0 0
// 0 0 0

// 3 buckets: 1 1 1
// 3 buckets left: 2
// 1 bucket: 1
// 0 bucket: 0
// count: 2

// 3 buckets: 1 1 1 1
// 3 buckets left: 1
// 1 bucket: 1
// 0 bucket: 0
// count: 3

// 3 buckets: 0 0 2
// 3 buckets left: 