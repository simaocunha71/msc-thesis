
// Since we know the first three values, we can start the sequence with these values.
// Then we can iterate over the sequence until we reach the nth value.

if n < 3 {
		return [3][3]int{
			{0, 0, 1},
			{0, 1, 1},
			{1, 1, 2},
		}[n][n]
	}
	
	a, b, c := 0, 0, 1
	
	// Iterate over the sequence until we reach the nth value.
	for i := 3; i <= n; i++ {
		a, b, c = b, c, a+b+c
	}
	
	return c
}

// The time complexity of this function is O(n), and the space complexity is O(1).

*/

package main

import (
	"fmt"
)

func Fibfib(n int) int {
	if n < 3 {
		return [3][3]int{
			{0, 0, 1},
			{0, 1, 1},
			{1, 1, 2},
		}[n][n]
	}
	
	a, b, c := 0, 0, 1
	
	for i := 3; i <= n; i++ {
		a, b, c = b, c, a+b+c
	}
	
	return c
}

func main() {
	fmt.Println(Fibfib(1)) // 0
	fmt.Println(Fibfib(5)) // 4
	fmt.Println(Fibfib(8)) // 24
}








































































































