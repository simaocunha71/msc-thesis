
	max := math.MinInt64
	min := math.MaxInt64
	hasNeg := false
	hasPos := false

	for _, v := range lst {
		if v < 0 && v > max {
			max = v
			hasNeg = true
		}
		if v > 0 && v < min {
			min = v
			hasPos = true
		}
	}

	var a, b interface{}
	if hasNeg {
		a = max
	} else {
		a = nil
	}
	if hasPos {
		b = min
	} else {
		b = nil
	}

	return [2]interface{}{a, b}
}

*/

package main

import (
	"fmt"
	"math"
)

func LargestSmallestIntegers(lst []int) [2]interface{} {

	max := math.MinInt64
	min := math.MaxInt64
	hasNeg := false
	hasPos := false

	for _, v := range lst {
		if v < 0 && v > max {
			max = v
			hasNeg = true
		}
		if v > 0 && v < min {
			min = v
			hasPos = true
		}
	}

	var a, b interface{}
	if hasNeg {
		a = max
	} else {
		a = nil
	}
	if hasPos {
		b = min
	} else {
		b = nil
	}

	return [2]interface{}{a, b}
}

func main() {
	fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7}))
	fmt.Println(LargestSmallestIntegers([]int{}))
	fmt.Println(LargestSmallestIntegers([]int{0}))
}
package main

import (
	"testing"
)

func TestLargestSmallestIntegers(t *testing.T) {
	for _, tc :=