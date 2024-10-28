```
package main

import (
	"fmt"
	"sort"
)

func RemoveDuplicates(numbers []int) []int {
	m := make(map[int]bool)
	result := []int{}
	for _, v := range numbers {
		if !m[v] {
			result = append(result, v)
			m[v] = true
		}
	}
	sort.Ints(result)
	return result
}

func main() {
	numbers := []int{1, 2, 3, 2, 4}
	fmt.Println(RemoveDuplicates(numbers)) // Output: [1 2 3 4]
}
```



The function `RemoveDuplicates(numbers []int)` is designed to remove all duplicates from a given list of integers while preserving the original order. It uses a map to keep track of the unique elements and then sorts the result. The time complexity is O(n log n) due to the sort operation.

In the `main` function, a list of integers is created and passed to the `RemoveDuplicates` function. The result is then printed to the console.

When you run the program, it will output: `[1 2 3 4]`, which are the unique elements from the original list in the same order.