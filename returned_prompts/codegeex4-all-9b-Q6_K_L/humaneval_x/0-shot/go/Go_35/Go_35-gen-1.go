You can use the sort package to sort the list in descending order and then return the first element. The sort.Ints function sorts a slice of ints in increasing order, but we can pass a custom function to sort in descending order by using the sort.Slice function. Here's how you can implement the MaxElement function:

```go
package main

import (
	"fmt"
	"sort"
)

func MaxElement(l []int) int {
	sort.Slice(l, func(i, j int) bool {
		return l[i] > l[j]
	})
	return l[0]
}

func main() {
	fmt.Println(MaxElement([]int{1, 2, 3})) // 3
	fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // 123
}
```

This implementation sorts the slice in-place, so it modifies the original slice. If you don't want to modify the original slice, you can create a copy of the slice before sorting it:

```go
func MaxElement(l []int) int {
	sorted := make([]int, len(l))
	copy(sorted, l)
	sort.Slice(sorted, func(i, j int) bool {
		return sorted[i] > sorted[j]
	})
	return sorted[0]
}
```

In this case, the sorted slice is a copy of the original slice, so the original slice is not modified.