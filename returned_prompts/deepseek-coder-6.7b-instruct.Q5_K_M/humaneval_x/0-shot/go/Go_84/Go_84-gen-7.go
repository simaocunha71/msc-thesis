    sum := 0
    for N != 0 {
        digit := N % 10
        sum += digit
        N /= 10
    }

B:
    return strconv.FormatInt(int64(sum), 2)
}

func main() {
    fmt.Println(Solve(1000))  // Output: 1
    fmt.Println(Solve(150))   // Output: 110
    fmt.Println(Solve(147))   // Output: 1100
}

*/

package main

import (
	"fmt"
	"strconv"
)

// Given a positive integer N, return the total sum of its digits in binary.
//
// Example
// For N = 1000, the sum of digits will be 1 the output should be "1".
// For N = 150, the sum of digits will be 6 the output should be "110".
// For N = 147, the sum of digits will be 12 the output should be "1100".
//
// Variables:
// @N integer
// Constraints: 0 ≤ N ≤ 10000.
// Output:
// a string of binary number
func Solve(N int) string {

	sum := 0
	for N != 0 {
		digit := N % 10
		sum += digit
		N /= 10
	}

	return strconv.FormatInt(int64(sum), 2)
}

func main() {
	fmt.Println(Solve(1000)) // Output: 1
	fmt.Println(Solve(150))  // Output: 110
	fmt.Println(Solve(147))  // Output: 1100
}

// Given a positive integer N, return the total sum of its digits in binary.
//
// Example
// For N = 1000, the sum of digits will be 1 the output should be "1".
// For