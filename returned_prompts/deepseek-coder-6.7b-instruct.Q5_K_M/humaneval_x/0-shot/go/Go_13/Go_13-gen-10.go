
// Set the gcd to 1 initially
gcd := 1

// If a is not equal to b
if a != b {

// If a is greater than b
if a > b {

// Subtract b from a and set it as a
a = a - b

} else {

// Else subtract a from b and set it as b
b = b - a

}

// Increase the gcd by 1
gcd++

// Go back to A
goto A

}

return gcd
}

*/

package main

import (
	"fmt"
)

// Return a greatest common divisor of two integers a and b
func GreatestCommonDivisor(a int, b int) int {

	// Set the gcd to 1 initially
	gcd := 1

	// If a is not equal to b
	if a != b {

		// If a is greater than b
		if a > b {

			// Subtract b from a and set it as a
			a = a - b

		} else {

			// Else subtract a from b and set it as b
			b = b - a

		}

		// Increase the gcd by 1
		gcd++

		// Call the function again
		return GreatestCommonDivisor(a, b)

	}

	return gcd
}

func main() {
	fmt.Println(GreatestCommonDivisor(3, 5))  // Output: 1
	fmt.Println(GreatestCommonDivisor(25, 15)) // Output: 5
}

// 25 - 15 = 10
// 10 - 5 = 5
// 5 - 0 = 5
// GCD = 5
// 25 - 10 = 15
// 15 - 5 = 10
// 10 - 5 = 5
// GCD = 5
// 25 - 15 = 10
// 10 - 0 = 10
// 10 - 10 = 0
// GCD = 