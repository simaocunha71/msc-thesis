To check if a string's length is a prime number, we need to first determine if the length is an odd number. If the length is even, it can't be a prime number. If it is odd, we can then check if it's divisible by any number other than 1 and itself. If it's not divisible by any other number, it is prime.

To check if a number is odd, we can use the modulus operator (%). If a number divided by 2 has a remainder of 1, it's odd.

To check if a number is prime, we can use a for loop to iterate through all numbers from 2 to the square root of the number (inclusive). If any of these numbers divide the original number evenly, it's not prime.

Here's how you can implement this in Go:

```go
package main

import (
	"fmt"
	"math"
)

func PrimeLength(s string) bool {
	length := len(s)
	if length%2 == 0 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(length)))+1; i++ {
		if length%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(PrimeLength("Hello")) // true
	fmt.Println(PrimeLength("abcdcba")) // true
	fmt.Println(PrimeLength("kittens")) // true
	fmt.Println(PrimeLength("orange")) // false
}
```

In this implementation, the PrimeLength function first checks if the length of the input string is even by using the modulus operator. If it is even, the function immediately returns false, as even numbers can't be prime.

If the length is odd, the function proceeds to the next step, which is to check if the length is divisible by any number from 2 to the square root of the length (inclusive). This is done using a for loop that iterates through all these numbers. If the length is divisible by any of these numbers, the function returns false.

If