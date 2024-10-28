```go
package main

import (
	"fmt"
	"math"
)

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

func CountUpTo(n int) []int {
	result := []int{}
	for i := 2; i < n; i++ {
		if isPrime(i) {
			result = append(result, i)
		}
	}
	return result
}

func main() {
	fmt.Println(CountUpTo(5))  // [2,3]
	fmt.Println(CountUpTo(11)) // [2,3,5,7]
	fmt.Println(CountUpTo(0))  // []
	fmt.Println(CountUpTo(20)) // [2,3,5,7,11,13,17,19]
	fmt.Println(CountUpTo(1))  // []
	fmt.Println(CountUpTo(18)) // [2,3,5,7,11,13,17]
}
```

Explanation:
This program defines a function `CountUpTo(n int) []int` that takes an integer `n` and returns an array of the first `n` integers that are prime numbers and less than `n`.

The `isPrime(num int) bool` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, it returns `false`; otherwise, it returns `true`.

The `CountUpTo(n int) []int` function iterates from 2 to `n-1` and checks each number with the `isPrime` function. If the number is prime, it appends it to the `result` array.

In the `main` function, we test the `CountUpTo` function with different inputs and print the results.

The time complexity of this solution is O(n * sqrt(n)) because we iterate over the numbers from 2 to `n-1` and for each number, we check if it's prime by iterating up to its square root. The space complexity is O(n) because we store the prime numbers in the `result` array.