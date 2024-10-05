    sum := 0
    for N > 0 {
        digit := N % 10
        sum += digit
        N /= 10
    }

    return strconv.FormatInt(int64(sum), 2)
}

func main()  {
    fmt.Println(Solve(1000))
    fmt.Println(Solve(150))
    fmt.Println(Solve(147))
}

*/

package main

import (
	"fmt"
	"strconv"
)

func Solve(N int) string {

	sum := 0
	for N > 0 {
		digit := N % 10
		sum += digit
		N /= 10
	}

	return strconv.FormatInt(int64(sum), 2)
}

func main() {
	fmt.Println(Solve(1000))
	fmt.Println(Solve(150))
	fmt.Println(Solve(147))
}

/*
Output:
1
110
1100
*/

// The output shows the sum of the digits of the number in binary form.

// The solution is to convert the integer to a string and iterate over each character. Then convert it back to an integer, sum up and finally convert that sum to a binary string.

// This solution assumes that the input N is always positive and less than or equal to 10000.

// The time complexity is O(log N) because we are iterating over the number of digits in N. The space complexity is O(1) because we are using a constant amount of space.

// The function returns a string that represents the sum of the digits of N in binary form.

// The function is named Solve because it solves the problem.

// The main function tests the Solve function with different inputs.

// The main function prints the binary string representation of the sum of the digits of the input numbers.

// The output of the main function is the binary string representation of the sum of the digits of the input numbers.

// The output matches