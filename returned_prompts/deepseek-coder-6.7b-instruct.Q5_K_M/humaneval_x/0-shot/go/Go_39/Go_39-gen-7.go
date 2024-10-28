	i := 1
	count := 0
	for {
		if isPrime(i) && isFibonacci(i) {
			count++
		}
		if count == n {
			return i
		}
		i++
	}
}

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func isFibonacci(n int) bool {
	if n == 0 {
		return false
	}
	x := (5 * n * n) + 4
	y := (5 * n * n) - 4
	return isPerfectSquare(x) || isPerfectSquare(y)
}

func isPerfectSquare(n int) bool {
	s := int(math.Sqrt(float64(n)))
	return s*s == n
}


*/
package main

import (
	"fmt"
)

// PrimeFib returns n-th number that is a Fibonacci number and it's also prime.
func PrimeFib(n int) int {
	i := 1
	count := 0
	for {
		if isPrime(i) && isFibonacci(i) {
			count++
		}
		if count == n {
			return i
		}
		i++
	}
}

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func isFibonacci(n int) bool {
	if n == 0 {
		return false
	}
	x := (5 * n * n) + 4
	y := (5 * n * n) - 4
	return isPerfectSquare(x) || isPerfectSquare(y)
}

func is