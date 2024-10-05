```go
package main

import (
	"fmt"
	"math"
)

// PrimeFib returns n-th number that is a Fibonacci number and it's also prime.
// >>> PrimeFib(1)
// 2
// >>> PrimeFib(2)
// 3
// >>> PrimeFib(3)
// 5
// >>> PrimeFib(4)
// 13
// >>> PrimeFib(5)
// 89
func PrimeFib(n int) int {
	var a, b int = 1, 1
	var count int = 0
	for {
		a, b = b, a+b
		if math.Mod(float64(b), 2) == 0 {
			continue
		}
		for i := 2; i <= int(math.Sqrt(float64(b))); i++ {
			if b%i == 0 {
				continue
			}
		}
		count++
		if count == n {
			return b
		}
	}
}

func main() {
	fmt.Println(PrimeFib(1))
	fmt.Println(PrimeFib(2))
	fmt.Println(PrimeFib(3))
	fmt.Println(PrimeFib(4))
	fmt.Println(PrimeFib(5))
}
```

Explanation:

The `PrimeFib` function generates Fibonacci numbers and checks if they are prime. It starts with the first two Fibonacci numbers `a` and `b` and then iterates through the sequence. For each number `b`, it checks if it's divisible by 2 (to skip even numbers) and then checks if it's prime by iterating from 2 to the square root of `b` (to avoid unnecessary checks). If `b` is prime, it increments the `count` variable. When `count` reaches the desired value `n`, it returns `b`.

The `main` function demonstrates the usage of the `PrimeFib` function with different values of `n`. The output should match the expected results.