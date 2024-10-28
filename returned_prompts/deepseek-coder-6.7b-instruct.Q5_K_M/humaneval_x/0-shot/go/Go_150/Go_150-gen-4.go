
// Your solution should be in the form of a function. 
// It should take three integer arguments n, x, y and return an integer. 

B:

// To solve the problem, you'll need to check if the number n is prime or not. 
// A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
// The simplest way to check if a number is prime is to iterate from 2 to the square root of the number and check if the number can be divided by any of these numbers. 
// If it can, then it's not a prime number. If it can't, then it is a prime number. 

C:

// If the number is prime, return the value of x. Otherwise, return the value of y. 

}

// Code:

package main

import (
	"fmt"
	"math"
)

func XOrY(n, x, y int) int {
	if isPrime(n) {
		return x
	} else {
		return y
	}
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
	fmt.Println(XOrY(7, 34, 12))  // 34
	fmt.Println(XOrY(15, 8, 5))   // 5
	fmt.Println(XOrY(2, 100, 200)) // 100
	fmt.Println(XOrY(4, 400, 500)) // 500
}

// Explanation:
// The function XOrY takes three integers n, x, y and returns x if n is prime, otherwise it returns y.
// The function isPrime checks if a number is prime or not. If the number is prime, it returns true, otherwise it returns false.
// The main