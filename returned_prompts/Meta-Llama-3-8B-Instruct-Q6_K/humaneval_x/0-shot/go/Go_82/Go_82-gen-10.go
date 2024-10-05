```go
package main

import (
	"fmt"
	"math"
)

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

func PrimeLength(s string) bool {
	return isPrime(len(s))
}

func main() {
	fmt.Println(PrimeLength("Hello"))  // true
	fmt.Println(PrimeLength("abcdcba")) // true
	fmt.Println(PrimeLength("kittens")) // true
	fmt.Println(PrimeLength("orange")) // false
}
```

The code defines a function `isPrime` that checks if a given number is prime. It does this by iterating from 2 up to the square root of the number and checking if the number is divisible by any of the values. If it is, the function returns `false`. If it reaches the end of the loop without finding a divisor, the function returns `true`.

The `PrimeLength` function simply calls `isPrime` with the length of the input string as an argument.

The `main` function demonstrates the usage of the `PrimeLength` function with the given examples. It prints the results of calling `PrimeLength` with the strings "Hello", "abcdcba", "kittens", and "orange". The output will be `true` for the first three strings and `false` for the last one, as expected.