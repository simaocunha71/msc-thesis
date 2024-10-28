```go
package main

import (
	"fmt"
)

func IncrList(l []int) []int {
	for i, v := range l {
		l[i] = v + 1
	}
	return l
}

func main() {
	fmt.Println(IncrList([]int{1, 2, 3})) // [2 3 4]
	fmt.Println(IncrList([]int{5, 3, 5, 2, 3, 3, 9, 0, 123})) // [6 4 6 3 4 4 10 1 124]
}
```


Explanation:
The provided Go function `IncrList` takes a slice of integers as an input, increments each element by 1, and returns the resulting slice.

 Inside the function, a range-based for loop is used to iterate over the input slice `l`. For each element `v` at index `i`, the element is incremented by 1 using the expression `v + 1` and the updated value is assigned back to the slice using `l[i] = v + 1`.

After incrementing all elements, the function returns the modified slice `l`.

In the `main` function, we call `IncrList` with two different input slices and print the resulting slices to demonstrate the functionality of the `IncrList` function. The output matches the expected results.