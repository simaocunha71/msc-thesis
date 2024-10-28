
	sum := func(x, y int) int {
		return x + y
	}
	
	switch x := x.(type) {
	case int:
		switch y := y.(type) {
		case int:
			switch z := z.(type) {
			case int:
				if x == sum(y,z) || y == sum(x,z) || z == sum(x,y) {
					return true
				}
			}
		}
	}
	
	return false
}

// Tests
func main() {
	fmt.Println(AnyInt(5, 2, 7)) // ➞ true
	fmt.Println(AnyInt(3, 2, 2)) // ➞ false
	fmt.Println(AnyInt(3, -2, 1)) // ➞ true
	fmt.Println(AnyInt(3.6, -2.2, 2)) // ➞ false
}
```

#### Golang Answer:
```go
package main

import "fmt"

// Create a function that takes 3 numbers.
// Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
// Returns false in any other cases.
func AnyInt(x, y, z float64) bool  {
    // if the sum of y and z is equal to x, or if the sum of x and z is equal to y, or if the sum of x and y is equal to z, return true
    if int(x)+int(y) == int(z) || int(x)+int(z) == int(y) || int(y)+int(z) == int(x) {
        return true
    }
    return false
}

func main() {
    fmt.Println(AnyInt(5, 2, 7)) // ➞ true
    fmt.Println(AnyInt(3, 2, 2)) // ➞ false
    fmt.Println(AnyInt(3, -2, 1)) // ➞ true
    fmt.Println