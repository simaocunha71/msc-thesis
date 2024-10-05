
// Given two positive integers a and b, return the even digits between a
// and b, in ascending order.
// 
// For example:
// GenerateIntegers(2, 8) ➞ [2, 4, 6, 8]
// GenerateIntegers(8, 2) ➞ [2, 4, 6, 8]
// GenerateIntegers(10, 14) ➞ []
func GenerateIntegers(a, b int) []int {

}

*/

package main

import (
	"fmt"
	"sort"
)

func GenerateIntegers(a, b int) []int {
	if a > b {
		a, b = b, a
	}

	result := make([]int, 0)
	for i := a; i <= b; i++ {
		if i%2 == 0 {
			result = append(result, i)
		}
	}

	sort.Ints(result)
	return result
}

func main() {
	fmt.Println(GenerateIntegers(2, 8))  // [2 4 6 8]
	fmt.Println(GenerateIntegers(8, 2))  // [2 4 6 8]
	fmt.Println(GenerateIntegers(10, 14)) // []
}
