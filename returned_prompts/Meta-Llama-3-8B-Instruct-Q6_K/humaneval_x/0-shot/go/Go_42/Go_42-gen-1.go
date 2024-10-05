```go
package main

import (
	"fmt"
)

func IncrList(l []int) []int {
	for i := range l {
		l[i]++
	}
	return l
}

func main() {
	fmt.Println(IncrList([]int{1, 2, 3})) // [2 3 4]
	fmt.Println(IncrList([]int{5, 3, 5, 2, 3, 3, 9, 0, 123})) // [6 4 6 3 4 4 10 1 124]
}
```

This program defines a function `IncrList` that takes a slice of integers as input and returns a new slice where each element is incremented by 1. The function uses a range loop to iterate over the input slice and increments each element in place. The modified slice is then returned.

In the `main` function, we call `IncrList` with two different input slices and print the results. The output shows that each element in the input slice is incremented by 1 as expected.