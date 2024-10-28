	a, b := 0, 1
	i := 0
	primeCount := 0
	result := 0
	for {
		a, b = b, a+b
		i++
		if isPrime(b) {
			primeCount++
			if primeCount == n {
				result = b
				break
			}
		}
	}
	return result
}

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	sqrtN := int(math.Sqrt(float6(n)))
	for i := 3; i <= sqrtN; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

*/

import (
	"math"
)

// PrimeFib returns n-th number that is a Fibonacci number and it's also prime.
func PrimeFib(n int) int {
	a, b := 0, 1
	i := 0
	primeCount := 0
	result := 0
	for {
		a, b = b, a+b
		i++
		if isPrime(b) {
			primeCount++
			if primeCount == n {
				result = b
				break
			}
		}
	}
	return result
}

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	sqrtN := int(math.Sqrt(float64(n)))
	for i := 3; i <= sqrtN; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}
package main

import (
	"fmt"
	"math"
)

/*

