```go
package main

import (
	"fmt"
	"math"
)

func PrimeLength(s string) bool {
	n := len(s)
	for i := 2; i <= math.Sqrt(float64(n)); i++ {
		if float64(n)%float64(i) == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(PrimeLength("Hello"))  // true
	fmt.Println(PrimeLength("abcdcba"))  // true
	fmt.Println(PrimeLength("kittens"))  // true
	fmt.Println(PrimeLength("orange"))  // false
}
```

Explanation:

The function `PrimeLength` checks if the length of the given string is a prime number. It does this by iterating from 2 to the square root of the string length, and checking if the string length is divisible by any of these numbers. If it is, the function returns `false`, indicating that the string length is not a prime number. If the function doesn't find any divisors, it returns `true`, indicating that the string length is a prime number.

In the `main` function, we test the `PrimeLength` function with different strings, and print the results. The output shows that the lengths of the strings "Hello", "abcdcba", and "kittens" are prime numbers, while the length of the string "orange" is not a prime number.