```go
package main

import (
	"fmt"
	"math"
)

func PrimeLength(s string) bool {
	l := len(s)
	if l <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(l))); i++ {
		if l%i == 0 {
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


In this solution, we first calculate the length of the input string `s`. If the length is less than or equal to 1, we immediately return `false` as 0 and 1 are not prime numbers.

Then, we iterate from 2 to the square root of the length of the string. If the length is divisible by any of these numbers, we return `false` as the length is not a prime number.

If the length is not divisible by any of these numbers, we return `true` as the length is a prime number. This solution has a time complexity of O(sqrt(n)) where n is the length of the string, as we are using a for loop that iterates up to the square root of the length. The space complexity is O(1) as we are using a constant amount of space to store the length and the iteration variable.