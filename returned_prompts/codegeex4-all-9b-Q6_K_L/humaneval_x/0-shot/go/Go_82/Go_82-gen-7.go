package main

import "fmt"

// isPrime checks if a number is prime
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

// PrimeLength checks if the length of a string is a prime number
func PrimeLength(s string) bool {
	return isPrime(len(s))
}

func main() {
	fmt.Println(PrimeLength("Hello")) // true
	fmt.Println(PrimeLength("abcdcba")) // true
	fmt.Println(PrimeLength("kittens")) // true
	fmt.Println(PrimeLength("orange")) // false
}