
	// Check if n is a prime number
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return y
		}
	}
	return x
}

func main() {

B:

	fmt.Println(XOrY(7, 34, 12))  //== 34
	fmt.Println(XOrY(15, 8, 5))  //== 5
}

*/

import (
	"fmt"
	"math"
)

// IsPrime checks if a given number n is a prime number
func IsPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

// XOrY returns x if n is a prime number, and y otherwise
func XOrY(n, x, y int) int {
	if IsPrime(n) {
		return x
	}
	return y
}

func main() {
	fmt.Println(XOrY(7, 34, 12))  //== 34
	fmt.Println(XOrY(15, 8, 5))   //== 5
}

// END OMIT
package main

import (
	"fmt"
	"math"
)

// START OMIT

// IsPrime checks if a given number n is a prime number
func IsPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

// END OMIT

func main() {
	fmt.Println(IsPrime(2))  //== true
	fmt.Println(IsPrime(4))  //== false
}

// START2 OMIT

// XOr