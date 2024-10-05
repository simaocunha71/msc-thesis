    return a * b / GreatestCommonDivisor(a, b)
}
*/
package main

import (
	"fmt"
)

func main() {
	fmt.Println(GreatestCommonDivisor(3, 5))
	fmt.Println(GreatestCommonDivisor(25, 15))
	fmt.Println(LeastCommonMultiple(3, 5))
	fmt.Println(LeastCommonMultiple(25, 15))
}

func GreatestCommonDivisor(a int, b int) int {
	for a != b {
		if a > b {
			a = a - b
		} else {
			b = b - a
		}
	}
	return a
}

func LeastCommonMultiple(a int, b int) int {
	return a * b / GreatestCommonDivisor(a, b)
}
package main

import (
	"fmt"
)

/*
