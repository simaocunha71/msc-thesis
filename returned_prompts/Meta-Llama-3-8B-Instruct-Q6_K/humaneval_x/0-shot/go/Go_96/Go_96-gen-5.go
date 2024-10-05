```go
package main

import (
	"fmt"
	"math"
)

func CountUpTo(n int) []int {
	if n <= 1 {
		return []int{}
	}
	primeNumbers := make([]int, 0, 10)
	for i := 2; i < n; i++ {
		if isPrime(i) {
			primeNumbers = append(primeNumbers, i)
			if len(primeNumbers) >= n {
				break
			}
		}
	}
	return primeNumbers
}

func isPrime(num int) bool {
	if num < 2 {
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
	fmt.Println(CountUpTo(5))  // [2,3]
	fmt.Println(CountUpTo(11)) // [2,3,5,7]
	fmt.Println(CountUpTo(0))  // []
	fmt.Println(CountUpTo(20)) // [2,3,5,7,11,13,17,19]
	fmt.Println(CountUpTo(1))  // []
	fmt.Println(CountUpTo(18)) // [2,3,5,7,11,13,17]
}
```

Explanation:
This program implements a function `CountUpTo` that takes an integer `n` as input and returns an array of the first `n` integers that are prime numbers and less than `n`. The function uses a helper function `isPrime` to check if a number is prime.

Here is the step-by-step explanation:

1. If `n` is less than or equal to 1, return an empty array.
2. Create a slice `primeNumbers` to store the prime numbers.
3. Iterate through the numbers from 2 to `n-1`. For each number `i`:
    - Check if `i` is prime using the `isPrime` function.
    - If `i` is prime, add it to the `primeNumbers` slice.
    - If the length of `primeNumbers` reaches `n`, break the loop.
4. Return the `primeNumbers` slice.

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values