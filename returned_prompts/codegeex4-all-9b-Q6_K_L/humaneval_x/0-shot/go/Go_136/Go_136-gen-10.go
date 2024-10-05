You can achieve this in Go by using the `sort` package to sort the list and then iterate over the sorted list to find the largest negative and smallest positive integers. Here's a possible implementation:

```go
package main

import (
	"fmt"
	"sort"
)

func LargestSmallestIntegers(lst []int) [2]interface{} {
	sort.Ints(lst) // Sort the list in ascending order

	var largestNegative *int
	var smallestPositive *int

	for _, num := range lst {
		if num < 0 {
			if largestNegative == nil || num > *largestNegative {
				largestNegative = &num
			}
		} else if num > 0 {
			if smallestPositive == nil || num < *smallestPositive {
				smallestPositive = &num
			}
		}
	}

	if largestNegative == nil {
		largestNegative = nil
	}
	if smallestPositive == nil {
		smallestPositive = nil
	}

	return [2]interface{}{largestNegative, smallestPositive}
}

func main() {
	fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7})) // Output: ([2]int)([1])
	fmt.Println(LargestSmallestIntegers([]int{})) // Output: ([2]int)([nil])
	fmt.Println(LargestSmallestIntegers([]int{0})) // Output: ([2]int)([nil])
}
```

This implementation first sorts the list in ascending order. Then, it iterates over the sorted list to find the largest negative and smallest positive integers. If no negative or positive integers are found, it sets the corresponding pointer to `nil`. Finally, it returns a tuple with the largest negative and smallest positive integers.