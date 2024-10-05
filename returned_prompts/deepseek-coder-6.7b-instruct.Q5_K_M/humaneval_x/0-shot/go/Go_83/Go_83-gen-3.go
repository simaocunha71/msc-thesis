    return int(math.Pow(2, float64(n-1)))
}

In the code above, we are using the math.Pow function to raise 2 to the power of n-1. This is equivalent to counting all the n-digit numbers where the first digit is 1. Since the 2^(n-1) gives us the count of numbers that start with 1, we can directly use it to solve the problem.
*/

package main

import (
	"fmt"
	"math"
)

// Given a positive integer n, return the count of the numbers of n-digit
// positive integers that start or end with 1.
func StartsOneEnds(n int) int {
	return int(math.Pow(2, float64(n-1)))
}

func main() {
	fmt.Println(StartsOneEnds(1)) // Output: 1
	fmt.Println(StartsOneEnds(2)) // Output: 2
	fmt.Println(StartsOneEnds(3)) // Output: 4
	fmt.Println(StartsOneEnds(4)) // Output: 8
}
package main

import (
	"fmt"
	"sort"
)

// Given an array of integers, find the first missing positive integer.
// The array can contain duplicates and negative numbers.
func FirstMissingPositive(nums []int) int {
	sort.Ints(nums)

	missing := 1
	for _, num := range nums {
		if num == missing {
			missing++
		}
	}

	return missing
}

func main() {
	fmt.Println(FirstMissingPositive([]int{1, 2, 0}))           // Output: 3
	fmt.Println(FirstMissingPositive([]int{3, 4, -1, 1}))       // Output: 2
	fmt.Println(FirstMissingPositive([]int{7, 8, 9, 11, 12}))   // Output: 1
	fmt.Println(FirstMissingPositive([]int{2, 