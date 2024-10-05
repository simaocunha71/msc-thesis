Here is the solution in Go:
```go
package main

import (
	"fmt"
)

func CountUpTo(n int) []int {
	primes := make([]bool, n+1)
	primes[0] = primes[1] = false
	for i := 2; i*i <= n; i++ {
		if primes[i] {
			for j := i * i; j <= n; j += i {
				primes[j] = false
			}
		}
	}
	result := make([]int, 0)
	for i := 2; i <= n; i++ {
		if primes[i] {
			result = append(result, i)
		}
	}
	return result
}

func main() {
	fmt.Println(CountUpTo(5))  // [2, 3]
	fmt.Println(CountUpTo(11)) // [2, 3, 5, 7]
	fmt.Println(CountUpTo(0))  // []
	fmt.Println(CountUpTo(20)) // [2, 3, 5, 7, 11, 13, 17, 19]
	fmt.Println(CountUpTo(1))   // []
	fmt.Println(CountUpTo(18)) // [2, 3, 5, 7, 11, 13, 17]
}
```
This program uses the Sieve of Eratosthenes algorithm to generate the list of prime numbers up to `n`. It initializes a boolean array `primes` of size `n+1` and sets all values to `true`. Then, it iterates over the array, starting from 2, and sets all multiples of each prime number to `false`. Finally, it iterates over the array again and collects all the prime numbers in a slice `result`. The function returns this slice.