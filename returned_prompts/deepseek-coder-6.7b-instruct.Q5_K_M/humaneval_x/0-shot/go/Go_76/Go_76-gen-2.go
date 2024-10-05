
    if x == 1 {
        return true
    }

    if n <= 1 {
        return false
    }

    for i := 2; i <= x; i++ {
        if math.Pow(float64(n), float64(i)) == float64(x) {
            return true
        }
    }
    return false
}

func main() {

    fmt.Println(IsSimplePower(1, 4)) //true
    fmt.Println(IsSimplePower(2, 2)) //true
    fmt.Println(IsSimplePower(8, 2)) //true
    fmt.Println(IsSimplePower(3, 2)) //false
    fmt.Println(IsSimplePower(3, 1)) //false
    fmt.Println(IsSimplePower(5, 3)) //false
}

*/
package main

import (
	"fmt"
	"math"
)

// IsSimplePower returns true if a number x is a simple power of n
func IsSimplePower(x int, n int) bool {

	if x == 1 {
		return true
	}

	if n <= 1 {
		return false
	}

	for i := 2; i <= x; i++ {
		if math.Pow(float64(n), float64(i)) == float64(x) {
			return true
		}
	}
	return false
}

func main() {

	fmt.Println(IsSimplePower(1, 4))  //true
	fmt.Println(IsSimplePower(2, 2))  //true
	fmt.Println(IsSimplePower(8, 2))  //true
	fmt.Println(IsSimplePower(3, 2))  //false
	fmt.Println(IsSimplePower(3, 1))  //false
	fmt.Println(IsSimplePower(5, 3))  //false
	fmt.Println(IsSimplePower(27, 3)) //true
	fmt.Println(IsSimplePower(16, 2)) //true
}
package main

import (