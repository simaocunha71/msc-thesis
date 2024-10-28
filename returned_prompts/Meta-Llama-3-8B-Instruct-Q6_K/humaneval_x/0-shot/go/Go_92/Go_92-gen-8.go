```go
package main

import (
	"fmt"
	"math"
)

func AnyInt(x, y, z interface{}) bool {
	// Check if all numbers are integers
	if _, ok := x.(int); !ok || _, ok = y.(int); !ok || _, ok = z.(int); !ok {
		return false
	}

	// Convert the interface{} values to int
	xInt, yInt, zInt := x.(int), y.(int), z.(int)

	// Check if one of the numbers is equal to the sum of the other two
	return xInt+yInt+zInt == xInt || xInt+yInt == zInt || xInt+zInt == yInt || yInt+zInt == xInt
}

func main() {
	fmt.Println(AnyInt(5, 2, 7)) // true
	fmt.Println(AnyInt(3, 2, 2)) // false
	fmt.Println(AnyInt(3, -2, 1)) // true
	fmt.Println(AnyInt(3.6, -2.2, 2)) // false
}
```


Explanation:

This function takes three numbers as input, and returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers. It returns false in any other cases.

Here's a breakdown of the function:

1. First, it checks if all numbers are integers by checking if they implement the `int` interface. If any of the numbers are not integers, the function returns false.
2. Then, it converts the interface{} values to int using type assertions.
3. Finally, it checks if one of the numbers is equal to the sum of the other two using the following conditions:
	* `xInt+yInt+zInt == xInt`
	* `xInt+yInt == zInt`
	* `xInt+zInt == yInt`
	* `yInt+zInt == xInt`
	* If any of these conditions are true, the function returns true. Otherwise, it returns false.

The function is tested in the main function with different inputs, and the results are printed to the console.