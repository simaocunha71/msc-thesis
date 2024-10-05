```go
package main

import (
	"fmt"
)

func MaxElement(l []int) int {
	max := l[0]
	for _, v := range l {
		if v > max {
			max = v
		}
	}
	return max
}

func main() {
	fmt.Println(MaxElement([]int{1, 2, 3}))  // Output: 3
	fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // Output: 123
}
```

Explanation:
The `MaxElement` function takes a slice of integers as input and returns the maximum element in the slice. It initializes the maximum element to the first element in the slice (`l[0]`). Then, it iterates over the slice using a range loop. If the current element is greater than the maximum element found so far, it updates the maximum element. Finally, it returns the maximum element.

In the `main` function, we test the `MaxElement` function with two different slices of integers. The first slice is `[1, 2, 3]`, which has a maximum element of `3`. The second slice is a larger slice with a mix of positive and negative numbers, which has a maximum element of `123`. The output of the program is the maximum element in each slice.