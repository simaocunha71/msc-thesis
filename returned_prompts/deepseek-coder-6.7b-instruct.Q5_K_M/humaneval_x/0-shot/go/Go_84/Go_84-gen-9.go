    sum := 0
    for N > 0 {
        sum += N % 10
        N /= 10
    }

    return strconv.FormatInt(int64(sum), 2)
}

func main() {
    fmt.Println(Solve(1000)) // should return 1
    fmt.Println(Solve(150))  // should return 110
    fmt.Println(Solve(147))  // should return 1100
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
	for N > 0 {
		sum += N % 10
		N /= 10
	}

	return strconv.FormatInt(int64(sum), 2)
}

func main() {
	fmt.Println(Solve(1000)) // should return 1
	fmt.Println(Solve(150))  // should return 110
	fmt.Println(Solve(147))  // should return 1100
}
package main

import (
	"testing"
)

type Test struct {
	input    int
	expected string
}

func TestSolve(t *testing.T) {

	tests := []Test{
		{1000, "1"},
		{150, "