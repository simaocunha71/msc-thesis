
// 1. Create an array to store the previous 4 Fib4 numbers
	previousFibs := make([]int, 4)

// 2. Initialize the base cases
	previousFibs[0] = 0
	previousFibs[1] = 0
	previousFibs[2] = 2
	previousFibs[3] = 0

	if n < 4 {
		return previousFibs[n]
	}

// 3. Iterate from 4 to n, adding the last 4 numbers in the array together to get the next Fib4 number
	for i := 4; i <= n; i++ {
		nextFib := previousFibs[0] + previousFibs[1] + previousFibs[2] + previousFibs[3]

// 4. Shift the array to the left, discarding the oldest Fib4 number, and add the new Fib4 number to the end
		copy(previousFibs[:], previousFibs[1:])
		previousFibs[3] = nextFib
	}

	return previousFibs[3]
}

// Testing
func main() {
	fmt.Println(Fib4(5)) // 4
	fmt.Println(Fib4(6)) // 8
	fmt.Println(Fib4(7)) // 14
}

// This solution has a time complexity of O(n) and a space complexity of O(1), which makes it very efficient.

*/

package main

import (
	"fmt"
)

// Fib4 function
func Fib4(n int) int {
	if n < 4 {
		switch n {
		case 0:
			return 0
		case 1:
			return 0
		case 2:
			return 2
		default:
			return 0
		}
	}

	a, b, c, d := 0, 0, 2, 0
	var next int

	for i := 4; i <= n; i++ {
		next = a + b + c +