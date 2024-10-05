You can use the following solution:
```go
import (
	"math"
)

func PrimeFib(n int) int {
	a, b := 0, 1
	count := 0
	for {
		a, b = b, a+b
		if isPrime(b) {
			count++
			if count == n {
				return b
			}
		}
	}
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
```
This solution uses a loop to generate Fibonacci numbers and checks each number to see if it's prime using the `isPrime` function. The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of the values. If the number is not divisible, it's prime. The function returns true if the number is prime and false otherwise.

You can call the `PrimeFib` function with a specific value of `n` to get the corresponding prime Fibonacci number. For example, `PrimeFib(1)` returns 2, `PrimeFib(2)` returns 3, `PrimeFib(3)` returns 5, and so on.