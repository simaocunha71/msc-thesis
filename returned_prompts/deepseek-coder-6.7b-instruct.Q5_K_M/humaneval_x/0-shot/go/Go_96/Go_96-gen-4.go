
// Check if n is less than 2
if n < 2 {
    return []int{}
}

// Initialize a slice to store the prime numbers
primes := []int{}

// Iterate over the numbers up to n
for i := 2; i < n; i++ {
    // Assume the number is prime
    isPrime := true

    // Check if the number is divisible by any number up to its square root
    for j := 2; j*j <= i; j++ {
        if i%j == 0 {
            isPrime = false
            break
        }
    }

    // If the number is prime, add it to the slice
    if isPrime {
        primes = append(primes, i)
    }
}

// Return the slice of prime numbers
return primes

}

This function works by iterating over the numbers from 2 to n (as 1 is not considered a prime number), and for each number, it checks if it is divisible by any number up to its square root. If it is not divisible by any of these numbers, it is considered a prime number and is added to the slice. The function then returns this slice.

*/

package main

import (
	"fmt"
)

func CountUpTo(n int) []int {
	if n < 2 {
		return []int{}
	}

	primes := []int{}
	for i := 2; i < n; i++ {
		isPrime := true
		for j := 2; j*j <= i; j++ {
			if i%j == 0 {
				isPrime = false
				break
			}
		}
		if isPrime {
			primes = append(primes, i)
		}
	}
	return primes
}

func main() {
	fmt.Println(CountUpTo(5))  // Output: [2 3]
	fmt.Println(CountUpTo(11)) // Output: [2 3 5 7]
	fmt.Println(CountUpTo(0))  // Output: []
	fmt.Println(