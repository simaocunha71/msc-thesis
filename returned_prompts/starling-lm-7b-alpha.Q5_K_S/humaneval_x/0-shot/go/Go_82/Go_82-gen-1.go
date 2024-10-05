To determine if a number is prime, we can use a simple function that checks all the numbers up to the square root of the number to see if it is divisible by any of them. If none of them are divisible, then the number is prime.

In this case, we can use the same approach to determine if the length of the string is prime. We can loop through all the numbers up to the square root of the string length and check if the length is divisible by any of them. If none of them are divisible, then the length is prime.

Here is a solution in Go:

```go
package main

import (
	"fmt"
	"math"
)

func PrimeLength(s string) bool {
	length := len(s)

	if length == 1 {
		return false
	}

	for i := 2; i <= int(math.Sqrt(float64(length))); i++ {
		if length%i == 0 {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(PrimeLength("Hello"))       // true
	fmt.Println(PrimeLength("abcdcba"))     // true
	fmt.Println(PrimeLength("kittens"))    // true
	fmt.Println(PrimeLength("orange"))     // false
}
```

This solution first checks if the length is 1, because the length of a string cannot be a prime number. Then it loops through all the numbers up to the square root of the length and checks if the length is divisible by any of them. If none of them are divisible, it returns true, indicating that the length is prime. Otherwise, it returns false.

The main function demonstrates the usage of the PrimeLength function with some example strings.

When you run this code, it will output:

```
true
true
true
false
```

This means that the lengths of the strings "Hello", "abcdcba", and "kittens" are prime, while the length of the string "orange" is not.

```

```

```

```

``