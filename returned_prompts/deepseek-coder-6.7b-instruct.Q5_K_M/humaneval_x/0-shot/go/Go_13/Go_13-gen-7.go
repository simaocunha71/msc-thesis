
// Start with a while loop
for b != 0 {
    // Set a to b and b to a mod b
    a, b = b, a%b
}

// Return a, which is now the greatest common divisor
return a
}

func main() {
    fmt.Println(GreatestCommonDivisor(3,5))
    fmt.Println(GreatestCommonDivisor(25,15))
}

*/
package main

import "fmt"

// GreatestCommonDivisor function
func GreatestCommonDivisor(a int, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	fmt.Println(GreatestCommonDivisor(3, 5))
	fmt.Println(GreatestCommonDivisor(25, 15))
}

// Output:
// 1
// 5
// Process finished with exit code 0
package main

import (
	"fmt"
	"math"
)

// 