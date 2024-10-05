    // Initialize sum
    sum := 0

B:
    // Loop through the list
    for i, v := range lst {

C:
        // Check if the index is multiple of 3
        if i%3 == 0 {
            // If it is, square the value
            sum += int(math.Pow(float64(v), 2))
        } else if i%4 == 0 {
            // If the index is not a multiple of 3 but is a multiple of 4, cube the value
            sum += int(math.Pow(float64(v), 3))
        } else {
            // If the index is not a multiple of 3 or 4, add the value as is
            sum += v
        }

    }

D:
    // Return the sum
    return sum
}

*/

import (
	"math"
)

func SumSquares(lst []int) int {
	sum := 0
	for i, v := range lst {
		if i%3 == 0 {
			sum += int(math.Pow(float64(v), 2))
		} else if i%4 == 0 {
			sum += int(math.Pow(float64(v), 3))
		} else {
			sum += v
		}
	}
	return sum
}

/*
func main() {
	fmt.Println(SumSquares([]int{1, 2, 3}))         // should return 9
	fmt.Println(SumSquares([]int{-1, -5, 2, -1, -5})) // should return -126
	fmt.Println(SumSquares([]int{}))                // should return 0
}
*/
package main

import (
	"fmt"
	"sort"
)

func main() {
	nums := []int{3, 0, 1}
	missing := getMissingNumber(nums)
	fmt.Println(missing)
}

func getMissingNumber(nums []int) int {
	