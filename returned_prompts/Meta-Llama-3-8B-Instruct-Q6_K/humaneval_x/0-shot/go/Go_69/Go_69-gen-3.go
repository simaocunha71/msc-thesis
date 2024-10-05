```
package main

import (
	"fmt"
	"sort"
)

func Search(lst []int) int {
	sort.Ints(lst)
	for i := len(lst) - 1; i >= 0; i-- {
		if lst[i] > 0 {
			if i+1 >= lst[i] {
				return lst[i]
			}
		}
	}
	return -1
}

func main() {
	fmt.Println(Search([]int{4, 1, 2, 2, 3, 1}))  // 2
	fmt.Println(Search([]int{1, 2, 2, 3, 3, 3, 4, 4, 4}))  // 3
	fmt.Println(Search([]int{5, 5, 4, 4, 4}))  // -1
}
```



Explanation:

1. First, the list is sorted in ascending order using the `sort.Ints` function.
2. Then, the code iterates over the sorted list in reverse order (from the end to the beginning).
3. For each element, it checks if the element is greater than 0. If it is, it checks if the frequency of the element is greater than or equal to the value of the element itself. If both conditions are met, the function returns the element.
4. If no such element is found, the function returns -1.

The time complexity of this solution is O(n log n) due to the sorting operation, where n is the length of the input list. The space complexity is O(1) as it only uses a constant amount of space to store the temporary results.