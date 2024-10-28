
}

*/

package main

import (
	"fmt"
	"sort"
)

type Point struct {
	x, y, val int
}

func minPath(grid [][]int, k int) []int {
	n := len(grid)
	points := make([]Point, 0, n*n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			points = append(points, Point{i, j, grid[i][j]})
		}
	}

	sort.Slice(points, func(i, j int) bool {
		return points[i].val < points[j].val
	})

	res := make([]int, k)
	for i := 0; i < k; i++ {
		res[i] = points[i].val
	}

	return res
}

func main() {
	fmt.Println(minPath([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, 3))
	fmt.Println(minPath([][]int{{5, 9, 3}, {4, 1, 6}, {7, 8, 2}}, 1))
}

// Output:
// [1, 2, 1]
// [1]
package main

import "fmt"

// Given an array of integers nums, you start with an initial positive value startValue.
// In each iteration, you calculate the step by step sum of the array's elements.
// If the sum is ever equal to startValue, you can choose to increment the startValue or you can choose to increment each of the array's elements.
// Given that you can perform either action as many times as you want, what is the minimum startValue that you need to make all the array's elements non-negative?

// Return the minimum startValue that you will need to make all the array's elements non-negative.

// Example:
// Input: nums = [-3,2,-3,4,2]
// Output