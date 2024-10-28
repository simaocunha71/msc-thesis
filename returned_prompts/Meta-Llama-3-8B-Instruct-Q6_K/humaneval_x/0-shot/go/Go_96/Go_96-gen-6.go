Here is the solution for the problem:

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
	primeNumbers := []int{}
	for i := 2; i < n; i++ {
		if isPrime(i) {
			primeNumbers = append(primeNumbers, i)
		}
	}
	return primeNumbers
}

func main() {
	fmt.Println(CountUpTo(5))  // [2, 3]
	fmt.Println(CountUpTo(11)) // [2, 3, 5, 7]
	fmt.Println(CountUpTo(0))  // []
	fmt.Println(CountUpTo(20)) // [2, 3, 5, 7, 11, 13, 17, 19]
	fmt.Println(CountUpTo(1))  // []
	fmt.Println(CountUpTo(18)) // [2, 3, 5, 7, 11, 13, 17]
}
```


This program defines a function `isPrime(num int) bool` to check if a number is prime. It then defines the `CountUpTo(n int) []int` function to find the prime numbers up to `n` and return them in an array. The main function is used to test the `CountUpTo` function with different inputs. The output of the program will be the expected result for each input.