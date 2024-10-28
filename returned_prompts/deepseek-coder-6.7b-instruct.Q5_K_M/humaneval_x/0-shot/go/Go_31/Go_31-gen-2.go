
// If the given number is less than 2, it is not prime.
	if n < 2 {
		return false
	}

	// If the given number is 2, it is prime.
	if n == 2 {
		return true
	}

	// If the given number is divisible by 2, it is not prime.
	if n % 2 == 0 {
		return false
	}

	// Check for divisibility by all odd numbers up to the square root of the given number.
	i := 3
	for i * i <= n {
		if n % i == 0 {
			return false
		}
		i += 2
	}

	// If no divisors found, the given number is prime.
	return true
}

*/

package main

import (
	"fmt"
)

func IsPrime(n int) bool {
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	i := 3
	for i*i <= n {
		if n%i == 0 {
			return false
		}
		i += 2
	}
	return true
}

func main() {
	fmt.Println(IsPrime(6))
	fmt.Println(IsPrime(101))
	fmt.Println(IsPrime(11))
	fmt.Println(IsPrime(13441))
	fmt.Println(IsPrime(61))
	fmt.Println(IsPrime(4))
	fmt.Println(IsPrime(1))
}

/*
Output:
false
true
true
true
true
false
false
*/

// This is a simple way to determine if a number is prime in Go.
// It works by checking for divisibility by all odd numbers up to the square root of the number.
// This is because a larger factor of the number would be a multiple of a smaller factor that has already been checked.
// This reduces the number of iterations and makes the function more efficient.
// The function returns true if the number is prime and false otherwise.
// Note that this