
Here is a solution in Go:

```go
package main

import (
	"fmt"
)

func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

func sum(n int) int {
	if n == 0 {
		return 0
	}
	return n + sum(n-1)
}

func F(n int) []int {
	res := make([]int, n)
	for i := 1; i <= n; i++ {
		if i%2 == 0 {
			res[i-1] = factorial(i)
		} else {
			res[i-1] = sum(i)
		}
	}
	return res
}

func main() {
	fmt.Println(F(5)) // prints [1 2 6 24 15]
}
```

The `factorial` function calculates the factorial of a number, and the `sum` function calculates the sum of numbers from 1 to a number. The `F` function uses these functions to calculate the values for the list based on whether the index is even or odd.