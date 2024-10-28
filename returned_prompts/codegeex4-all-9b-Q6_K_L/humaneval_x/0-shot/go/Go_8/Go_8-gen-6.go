The following function should fulfill your requirements:

```go
func SumProduct(numbers []int) [2]int {
    sum := 0
    product := 1
    for _, num := range numbers {
        sum += num
        product *= num
    }
    return [2]int{sum, product}
}
```

The function `SumProduct` takes a slice of integers `numbers` and calculates the sum and product of all the integers in the slice. It initializes `sum` to 0 and `product` to 1. Then it iterates over each element `num` in `numbers`, adding `num` to `sum` and multiplying `num` with `product`. Finally, it returns a two-element array `[2]int` consisting of `sum` and `product`.

Here's how you can test the function:

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
	fmt.Println(SumProduct([]int{}))         // Output: [0 1]
	fmt.Println(SumProduct([]int{1, 2, 3, 4})) // Output: [10 24]
}
```

The first call to `SumProduct` with an empty slice returns `[0 1]`, and the second call with a non-empty slice returns `[10 24]`.