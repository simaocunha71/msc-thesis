package main

import (
	"fmt"
)

// isPrime checks if a number is prime
func isPrime(num int) bool {
	if num <= 1 {
		return false
	}
	for i := 2; i*i <= num; i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}

// primeFib returns the n-th prime Fibonacci number
func primeFib(n int) int {
	count := 0
	a, b := 0, 1
	for count < n {
		if isPrime(a) {
			count++
		}
		if count == n {
			return a
		}
		a, b = b, a+b
	}
	return -1 // not found
}

func main() {
	fmt.Println(primeFib(1)) // 2
	fmt.Println(primeFib(2)) // 3
	fmt.Println(primeFib(3)) // 5
	fmt.Println(primeFib(4)) // 13
	fmt.Println(primeFib(5)) // 89
}

