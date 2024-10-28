```go
package main

import (
	"fmt"
	"math"
)

func AnyInt(x, y, z interface{}) bool {
	// Check if all inputs are integers
	if _, ok := x.(int); !ok {
		return false
	}
	if _, ok := y.(int); !ok {
		return false
	}
	if _, ok := z.(int); !ok {
		return false
	}

	// Check if one of the numbers is equal to the sum of the other two
	if x.(int)+y.(int) == z.(int) {
		return true
	}
	if x.(int)+z.(int) == y.(int) {
		return true
	}
	if y.(int)+z.(int) == x.(int) {
		return true
	}

	return false
}

func main() {
	fmt.Println(AnyInt(5, 2, 7)) // true
	fmt.Println(AnyInt(3, 2, 2)) // false
	fmt.Println(AnyInt(3, -2, 1)) // true
	fmt.Println(AnyInt(3.6, -2.2, 2)) // false
}
```

The function `AnyInt` takes three interface{} arguments. It first checks if all inputs are integers using type assertions. If any of the inputs are not integers, it immediately returns `false`.

Then it checks if one of the numbers is equal to the sum of the other two. It uses the type assertion to convert the interface{} values to int and then checks for equality. If it finds a match, it returns `true`.

If it doesn't find a match, it returns `false`. The function uses the `math` package to check for equality, but in this case, it's not necessary, as the type assertions ensure that the inputs are integers.