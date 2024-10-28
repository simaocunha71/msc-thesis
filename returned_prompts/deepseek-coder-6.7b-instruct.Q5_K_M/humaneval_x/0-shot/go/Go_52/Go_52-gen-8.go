
}
*/

package main

import "fmt"

func BelowThreshold(l []int, t int) bool {
	for _, num := range l {
		if num >= t {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(BelowThreshold([]int{1, 2, 4, 10}, 100)) // true
	fmt.Println(BelowThreshold([]int{1, 20, 4, 10}, 5))  // false
}
package main

import (
	"fmt"
	"strings"
)

func AboveAverage(l []int) (int, bool) {
	total := 0
	aboveAverage := 0
	aboveAvgExists := false

	for _, num := range l {
		total += num
	}

	avg := total / len(l)

	for _, num := range l {
		if num > avg {
			aboveAverage += num
			aboveAvgExists = true
		}
	}

	return aboveAverage, aboveAvgExists
}

func main() {
	result, exists := AboveAverage([]int{1, 2, 3, 4, 5})
	if exists {
		fmt.Println("Sum of numbers above average:", result)
	} else {
		fmt.Println("No numbers are above average")
	}
}

// Test cases:
// 1. AboveAverage([1, 2, 3, 4, 5]) -> 15, true
// 2. AboveAverage([10, 10, 10, 10, 10]) -> 0, false
// 3. AboveAverage([5, 10, 15, 20, 25]) -> 40, true
// 4. AboveAverage([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) -> 35, true
// 5