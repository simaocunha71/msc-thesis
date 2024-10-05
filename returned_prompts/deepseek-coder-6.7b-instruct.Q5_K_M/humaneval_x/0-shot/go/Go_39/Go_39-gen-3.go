	i := 1
	j := 1
	count := 0

B:
	for {
		temp := i + j
		i = j
		j = temp

		if isPrime(j) {
			count++
		}

		if count == n {
			return j
		}
	}

	return -1
}

func isPrime(n int) bool {
	if n < 2 {
		return false
	}

	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}

	return true
}
```

## Test

```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println(PrimeFib(1)) // 2
	fmt.Println(PrimeFib(2)) // 3
	fmt.Println(PrimeFib(3)) // 5
	fmt.Println(PrimeFib(4)) // 13
	fmt.Println(PrimeFib(5)) // 89
}
```

## Complexity Analysis

- Time Complexity: O(n^2)
- Space Complexity: O(1)

In the worst case scenario, we may have to calculate all Fibonacci numbers up to the nth prime number, which takes O(n^2) time.

The space complexity is constant, as we only store a constant amount of variables.

## Optimization

If we want to improve the performance, we can use a method to generate prime numbers specifically, such as the Sieve of Eratosthenes method. This method can generate all prime numbers up to a given limit in linear time.

However, in this case, we need to generate Fibonacci numbers and check if they are prime, so the time complexity will be O(n^2).

The space complexity will still be constant, as we only store a constant amount of variables.

## References

1. [Fibonacci sequence](https://en.wikipedia.org/wiki/