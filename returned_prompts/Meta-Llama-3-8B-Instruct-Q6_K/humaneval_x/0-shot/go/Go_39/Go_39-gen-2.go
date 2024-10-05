The problem is asking for the nth number in the Fibonacci sequence that is also a prime number. This problem can be solved by generating Fibonacci numbers and checking if they are prime.

Here is a possible solution in Go:

```go
package main

import (
	"fmt"
	"math"
)

// IsPrime checks if a number is prime
func IsPrime(n int) bool {
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

// PrimeFib returns n-th number that is a Fibonacci number and it's also prime.
func PrimeFib(n int) int {
	a, b := 0, 1
	count := 0
	for {
		a, b = b, a+b
		if IsPrime(b) {
			count++
			if count == n {
				return b
			}
		}
	}
}

func main() {
	fmt.Println(PrimeFib(1)) // Output: 2
	fmt.Println(PrimeFib(2)) // Output: 3
	fmt.Println(PrimeFib(3)) // Output: 5
	fmt.Println(PrimeFib(4)) // Output: 13
	fmt.Println(PrimeFib(5)) // Output: 89
}
```

This solution uses the `IsPrime` function to check if a number is prime, and the `PrimeFib` function to generate Fibonacci numbers and check if they are prime. The `main` function is used to test the `PrimeFib` function with different values of `n`.