
// We use the math package to use the Sqrt function
// We also use the math.Pow function to check if the power of n is equal to the square root of x.

// We cast the int values to float64 because the math.Pow and math.Sqrt functions operate on float64 types.

    sqrt := math.Sqrt(float64(x))
    power := math.Pow(float64(n),sqrt)

    // We use the == operator to check if the power of n is equal to the square root of x.
    if power == float64(x) {
        return true
    }
    return false
}

*/

package main

import (
	"fmt"
	"math"
)

func IsSimplePower(x int, n int) bool {
	sqrt := math.Sqrt(float64(x))
	power := math.Pow(float64(n), sqrt)
	if power == float64(x) {
		return true
	}
	return false
}

func main() {
	fmt.Println(IsSimplePower(1, 4))   // true
	fmt.Println(IsSimplePower(2, 2))   // true
	fmt.Println(IsSimplePower(8, 2))   // true
	fmt.Println(IsSimplePower(3, 2))   // false
	fmt.Println(IsSimplePower(3, 1))   // false
	fmt.Println(IsSimplePower(5, 3))   // false
}
/*
