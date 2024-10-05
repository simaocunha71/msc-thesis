```go
package main

import (
	"fmt"
	"math"
)

func CountUpTo(n int) []int {
	var primes []int
	for i := 2; i < n; i++ {
		if IsPrime(i) {
			primes = append(primes, i)
		}
	}
	return primes
}

func IsPrime(num int) bool {
	if num <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(CountUpTo(5))  // [2,3]
	fmt.Println(CountUpTo(11)) // [2,3,5,7]
	fmt.Println(CountUpTo(0))  // []
	fmt.Println(CountUpTo(20)) // [2,3,5,7,11,13,17,19]
	fmt.Println(CountUpTo(1))   // []
	fmt.Println(CountUpTo(18))  // [2,3,5,7,11,13,17]
}
```

This program defines a function `CountUpTo` that takes an integer `n` as input and returns a slice of prime numbers less than `n`. The `CountUpTo` function uses a loop to iterate over the numbers from 2 to `n-1`. For each number, it checks if it is prime using the `IsPrime` function. If the number is prime, it is added to the `primes` slice. The `IsPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is not divisible, it is prime. The `main` function tests the `CountUpTo` function with different inputs and prints the results.