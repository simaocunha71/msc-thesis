    strN := strconv.Itoa(n)
    result := 1

B:
    for _, c := range strN {
        digit, _ := strconv.Atoi(string(c))
        if digit % 2 != 0 {
            result *= digit
        }
    }

    return result
}

func main() {
    fmt.Println(Digits(1))  // 1
    fmt.Println(Digits(4))  // 0
    fmt.Println(Digits(235)) // 15
}

*/

package main

import (
	"fmt"
	"strconv"
)

// Given a positive integer n, return the product of the odd Digits.
// Return 0 if all Digits are even.
// For example:
// Digits(1)  == 1
// Digits(4)  == 0
// Digits(235) == 15
func Digits(n int) int {
	strN := strconv.Itoa(n)
	result := 1

	for _, c := range strN {
		digit, _ := strconv.Atoi(string(c))
		if digit%2 != 0 {
			result *= digit
		}
	}

	return result
}

func main() {
	fmt.Println(Digits(1))  // 1
	fmt.Println(Digits(4))  // 0
	fmt.Println(Digits(235)) // 15
}
/*
