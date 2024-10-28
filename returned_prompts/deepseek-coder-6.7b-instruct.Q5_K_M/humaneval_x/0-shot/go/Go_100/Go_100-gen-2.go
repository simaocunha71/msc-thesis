
	result := make([]int, n)

	for i := 0; i < n; i++ {
		if n%2 != 0 {
			result[i] = n + i*2
		} else {
			result[i] = n + (i+1)*2 - 1
		}
	}

	return result
}

*/

package main

import (
	"fmt"
)

func MakeAPile(n int) []int {

	result := make([]int, n)

	for i := 0; i < n; i++ {
		if n%2 != 0 {
			result[i] = n + i*2
		} else {
			result[i] = n + (i+1)*2 - 1
		}
	}

	return result
}

func main() {
	fmt.Println(MakeAPile(3))
}

// Output:
// [3, 5, 7]

/*

Explanation:

We first create an empty slice of length n.

Then we loop over each element in the slice, and for each index i, if n is odd we set the element at index i in the slice to n + i*2.

If n is even, we set the element at index i in the slice to n + (i+1)*2 - 1.

Finally we return the slice.

*/
/*

Create a function that takes an array of numbers and returns the second largest number in the array.

Examples:

SecondLargest([10, 20, 40, 50, 30]) ➞ 40

SecondLargest([25, 15, 50, 40, 35]) ➞ 40

SecondLargest([10, 10, 10, 10, 10]) ➞ "No second largest number"

Notes:

- If there is no second largest number, return the string "No second largest number".
- All numbers in the array will be positive.
- The array will