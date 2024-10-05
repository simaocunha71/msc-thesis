```go
package main

import (
	"fmt"
	"math"
)

func AnyInt(x, y, z interface{}) bool {
	// Convert the interface{} types to float64
	fx, fy, fz := float64(x.(int)), float64(y.(int)), float64(z.(int))

	// Check if the sum of the other two numbers is equal to one of the numbers
	if math.Abs(fx-fy-fz) < 1e-9 {
		return true
	}
	if math.Abs(fx-fz-fy) < 1e-9 {
		return true
	}
	if math.Abs(fy-fx-fz) < 1e-9 {
		return true
	}
	// Check if all numbers are integers
	if fx != math.Trunc(fx) || fy != math.Trunc(fy) || fz != math.Trunc(fz) {
		return false
	}
	return false
}

func main() {
	fmt.Println(AnyInt(5, 2, 7))  // true
	fmt.Println(AnyInt(3, 2, 2))  // false
	fmt.Println(AnyInt(3, -2, 1)) // true
	fmt.Println(AnyInt(3.6, -2.2, 2))  // false
}
```







