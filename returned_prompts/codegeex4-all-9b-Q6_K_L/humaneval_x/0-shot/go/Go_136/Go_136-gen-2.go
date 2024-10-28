You can use the `sort` package to sort the list and then return the first and last elements of the sorted list. Here's an example implementation:

```go
package main

import (
	"fmt"
	"sort"
)

func LargestSmallestIntegers(lst []int) [2]interface{} {
	if len(lst) == 0 {
		return [2]interface{}{nil, nil}
	}

	sort.Ints(lst)

	var largestNegative, smallestPositive interface{}

	for _, num := range lst {
		if num < 0 {
			largestNegative = num
			break
		}
	}

	for i := len(lst) - 1; i >= 0; i-- {
		if lst[i] > 0 {
			smallestPositive = lst[i]
			break
		}
	}

	return [2]interface{}{largestNegative, smallestPositive}
}

func main() {
	fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7})) // Output: [2]int{nil, 1}
	fmt.Println(LargestSmallestIntegers([]int{}))                   // Output: [2]int{nil, nil}
	fmt.Println(LargestSmallestIntegers([]int{0}))                  // Output: [2]int{nil, nil}
}
```

In this implementation, we first check if the list is empty and return `(nil, nil)` if it is. Then, we use the `sort.Ints` function to sort the list in ascending order. We then iterate through the sorted list to find the largest negative integer and the smallest positive integer. Finally, we return these values as a tuple using the `[2]interface{}` type.