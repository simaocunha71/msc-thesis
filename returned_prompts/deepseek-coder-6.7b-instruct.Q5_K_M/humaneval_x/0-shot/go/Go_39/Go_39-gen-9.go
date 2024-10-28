	i := 1
	j := 2
	count := 2
	primeCounter := 0

B:
	if primeCheck(i) {
		primeCounter++
	}
	if primeCounter == n {
		return i
	}

	i, j = j, i+j
	goto B
}

func primeCheck(n int) bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}

	for i := 3; i <= int(math.Sqrt(float6y)); i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

*/

package main

import (
	"fmt"
	"math"
)

// PrimeFib returns n-th number that is a Fibonacci number and it's also prime.
func PrimeFib(n int) int {

	i := 1
	j := 2
	primeCounter := 0

	for {
		if primeCheck(i) {
			primeCounter++
		}
		if primeCounter == n {
			return i
		}

		i, j = j, i+j
	}
}

func primeCheck(n int) bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}

	for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(PrimeFib(1)) // 2
	fmt.Println(PrimeFib(2)) // 3
	fmt.Println(PrimeFib(3)) // 5
	fmt.Println(PrimeFib(4)) // 13
	fmt.Println(PrimeFib(5)) // 89
}
package main

import (
