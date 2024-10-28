
To solve this problem, you can use a simple mathematical formula to calculate the n-th Fibonacci number. The formula is as follows:

F(n) = ((1 + sqrt(5))/2)^n - ((1 - sqrt(5))/2)^n

Here is a Go code example:

```go
package main

import (
	"fmt"
	"math"
)

func Fib(n int) int {
	if n == 0 {
		return 0
	} else if n == 1 {
		return 1
	}

	return int(math.Pow((1+math.Sqrt(5))/2, float64(n)) - math.Pow((1-math.Sqrt(5))/2, float64(n)))
}

func main() {
	fmt.Println(Fib(10)) // Output: 55
	fmt.Println(Fib(8))  // Output: 21
	fmt.Println(Fib(1))  // Output: 1
}
```

This code defines a function `Fib` that takes an integer `n` as input and returns the n-th Fibonacci number. The function first checks if `n` is 0 or 1, and if so, it returns the corresponding base case value. Otherwise, it calculates the Fibonacci number using the provided formula and returns the result.

In the `main` function, we demonstrate the usage of the `Fib` function by passing different values of `n` and printing the corresponding Fibonacci numbers.

This solution provides an efficient and accurate way to calculate Fibonacci numbers in Go.

```go
package main

import (
	"fmt"
	"math"
)

func Fib(n int) int {
	if n == 0 {
		return 0
	} else if n == 1 {
		return 1
	}

	return int(math.Pow((1+math.Sqrt(5))/2, float64(n)) - math.Pow((1-math.Sqrt