```go
package main

import (
	"fmt"
	"math"
)

func CountUpTo(n int) []int {
	var result []int
	for i := 2; i < n; i++ {
		if isPrime(i) {
			result = append(result, i)
		}
	}
	return result
}

func isPrime(num int) bool {
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
	fmt.Println(CountUpTo(5)) // [2,3]
	fmt.Println(CountUpTo(11)) // [2,3,5,7]
	fmt.Println(CountUpTo(0)) // []
	fmt.Println(CountUpTo(20)) // [2,3,5,7,11,13,17,19]
	fmt.Println(CountUpTo(1)) // []
	fmt.Println(CountUpTo(18)) // [2,3,5,7,11,13,17]
}
```

Explanation:
The program defines a function `CountUpTo` that takes an integer `n` as input and returns a slice of prime numbers less than `n`.

 Inside the `CountUpTo` function, it iterates from `2` to `n-1` and checks if each number is prime using the `isPrime` function. If the number is prime, it appends it to the `result` slice.

The `isPrime` function checks if a number is prime by iterating from `2` to the square root of the number and checking if the number is divisible by any of the numbers in that range. If it is, the function returns `false`, indicating that the number is not prime. If the number is not divisible by any of the numbers in that range, the function returns `true`, indicating that the number is prime.

In the `main` function, the program tests the `CountUpTo` function with different inputs and prints the results.