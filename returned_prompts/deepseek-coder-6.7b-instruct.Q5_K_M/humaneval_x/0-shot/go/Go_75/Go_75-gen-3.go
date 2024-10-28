
// Write your code here

}
*/

package main

import (
	"fmt"
	"math"
)

func IsMultiplyPrime(a int) bool {
	count := 0
	for i := 2; i <= int(math.Sqrt(float64(a))); i++ {
		if a%i == 0 {
			for a%i == 0 {
				a = a / i
				count++
			}
			if isPrime(i) == false || count > 3 {
				return false
			}
		}
	}
	if a != 1 && isPrime(a) {
		count++
	}
	return count == 3
}

func isPrime(n int) bool {
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

func main() {
	fmt.Println(IsMultiplyPrime(30)) // should return true
	fmt.Println(IsMultiplyPrime(60)) // should return false
	fmt.Println(IsMultiplyPrime(105)) // should return true
	fmt.Println(IsMultiplyPrime(135)) // should return false
}
/*
