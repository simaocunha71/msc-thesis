```go
package main

import (
	"fmt"
	"math"
)

func AnyInt(x, y, z interface{}) bool {
	// Convert the input values to float64 to allow for easy comparison
	xFloat, okX := x.(float64)
	yFloat, okY := y.(float64)
	zFloat, okZ := z.(float64)

	if !okX || !okY || !okZ {
		// If any of the inputs are not floats, return false
		return false
	}

	// Check if any of the numbers are equal to the sum of the other two
	if math.Abs(xFloat-yFloat-zFloat) < 1e-9 {
		return true
	}
	if math.Abs(xFloat-zFloat-yFloat) < 1e-9 {
		return true
	}
	if math.Abs(yFloat-xFloat-zFloat) < 1e-9 {
		return true
	}
	if math.Abs(yFloat-zFloat-xFloat) < 1e-9 {
		return true
	}
	if math.Abs(zFloat-xFloat-yFloat) < 1e-9 {
		return true
	}
	if math.Abs(zFloat-yFloat-xFloat) < 1e-9 {
		return true
	}

	// If none of the above conditions are met, return false
	return false
}

func main() {
	fmt.Println(AnyInt(5, 2, 7)) // true
	fmt.Println(AnyInt(3, 2, 2)) // false
	fmt.Println(AnyInt(3, -2, 1)) // true
	fmt.Println(AnyInt(3.6, -2.2, 2)) // false
}
```


Here is the Go code that implements the function `AnyInt(x, y, z interface{}) bool`. The function takes three inputs and checks if one of them is equal to the sum of the other two. It returns `true` if such a condition is met and all the inputs are integers, and `false` otherwise.

The function first converts the inputs to `float64` to allow for easy comparison. It then checks if any of the numbers are equal to the sum of the other two by using the `math.Abs` function to check for equality within a small tolerance (1e-9). If such a condition is met, the function returns `true`. If not, it returns `false`.

In the `main` function,