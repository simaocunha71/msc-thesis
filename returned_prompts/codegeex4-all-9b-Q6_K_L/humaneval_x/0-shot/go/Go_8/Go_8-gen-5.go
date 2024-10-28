You can solve this by using the built-in functions `sum` and `prod` from the `math` package in Go. Here is a possible solution:

```go
package main

import (
	"fmt"
	"math"
)

func SumProduct(numbers []int) (int, int) {
	sum := math.Sum(numbers)
	product := math.Prod(numbers)
	return sum, product
}

func main() {
	fmt.Println(SumProduct([]int{}))          // Output: 0 1
	fmt.Println(SumProduct([]int{1, 2, 3, 4})) // Output: 10 24
}
```

In this solution, the `SumProduct` function takes a slice of integers as input and returns a tuple consisting of the sum and product of all the integers in the list. The `math.Sum` function calculates the sum of all the integers in the list and the `math.Prod` function calculates the product of all the integers in the list. If the list is empty, the sum is 0 and the product is 1, as specified in the problem statement.