```go
package main

import (
	"fmt"
)

func PrimeLength(s string) bool {
	n := len(s)
	for i := 2; i <= n/2; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(PrimeLength("Hello"))  // true
	fmt.Println(PrimeLength("abcdcba")) // true
	fmt.Println(PrimeLength("kittens")) // true
	fmt.Println(PrimeLength("orange")) // false
}
```
This program defines a function `PrimeLength` that takes a string `s` and returns `true` if the length of the string is a prime number, and `false` otherwise. The function works by iterating from 2 to the square root of the length of the string, and checking if the length is divisible by any of these numbers. If it is, the function returns `false`. If it is not divisible by any of these numbers, the function returns `true`.

The `main` function is used to test the `PrimeLength` function with different inputs. The output of the program is:
```
true
true
true
false
```
which matches the expected results.