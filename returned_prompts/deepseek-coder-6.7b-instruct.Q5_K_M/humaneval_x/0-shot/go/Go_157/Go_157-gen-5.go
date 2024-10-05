
// Here we calculate the squares of the sides
squareA := a * a
squareB := b * b
squareC := c * c

B:

// Now we check if the sum of squares of two sides is equal to square of the third side
// This is the property of Pythagoras that a square of the hypotenuse is equal to the sum of squares of other two sides
if squareA + squareB == squareC || squareB + squareC == squareA || squareC + squareA == squareB {
return true
}

C:

return false
}
*/
package main

import "fmt"

func RightAngleTriangle(a, b, c int) bool {
	squareA := a * a
	squareB := b * b
	squareC := c * c

	if squareA+squareB == squareC || squareB+squareC == squareA || squareC+squareA == squareB {
		return true
	}

	return false
}

func main() {
	fmt.Println(RightAngleTriangle(3, 4, 5)) // Expected output: true
	fmt.Println(RightAngleTriangle(1, 2, 3)) // Expected output: false
}
package main

import (
	"fmt"
)

// 