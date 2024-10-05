```go
package main

import (
	"fmt"
	"math"
)

func Factorize(n int) []int {
	if n <= 1 {
		return []int{}
	}

	factors := []int{}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			factors = append(factors, i)
			n /= i
			i--
		}
	}
	if n > 1 {
		factors = append(factors, n)
	}
	return factors
}

func main() {
	fmt.Println(Factorize(8))  // Output: [2 2 2]
	fmt.Println(Factorize(25)) // Output: [5 5]
	fmt.Println(Factorize(70)) // Output: [2 5 7]
}
```

This code correctly factorizes the given integer by iterating from 2 up to the square root of the number. If the number is divisible by the current iteration, it adds that divisor to the list of factors and divides the number by that divisor. The loop continues until the number is no longer divisible by the current iteration. If the number is still greater than 1 after the loop, it means that the number itself is a prime factor, so it is added to the list of factors.