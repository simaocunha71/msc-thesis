```go
package main

import (
	"fmt"
)

func SumProduct(numbers []int) [2]int {
	sum := 0
	product := 1
	for _, num := range numbers {
		sum += num
		product *= num
	}
	return [2]int{sum, product}
}

func main() {
	fmt.Println(SumProduct([]int{}))  // (0, 1)
	fmt.Println(SumProduct([]int{1, 2, 3, 4}))  // (10, 24)
}
```

Explanation:

In this solution, we define a function called `SumProduct` that takes a slice of integers as input. It initializes two variables, `sum` and `product`, to zero and one respectively. Then it iterates over the input slice using a range-based `for` loop, adding each number to `sum` and multiplying each number with `product`. Finally, it returns a tuple (or a slice of two integers) containing the sum and product of the input numbers.

In the `main` function, we test the `SumProduct` function with an empty slice and a slice containing the numbers 1, 2, 3, and 4. The output is as expected: `(0, 1)` for the empty slice and `(10, 24)` for the slice with the numbers 1, 2, 3, and 4.