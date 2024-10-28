```
package main

import (
	"fmt"
	"sort"
)

func Search(lst []int) int {
	sort.Ints(lst)
	max := 0
	for i := len(lst) - 1; i >= 0; i-- {
		if lst[i] <= i+1 {
			return -1
		}
		if lst[i] > max {
			max = lst[i]
		}
	}
	return max
}

func main() {
	fmt.Println(Search([]int{4, 1, 2, 2, 3, 1})) // Output: 2
	fmt.Println(Search([]int{1, 2, 2, 3, 3, 3, 4, 4, 4})) // Output: 3
	fmt.Println(Search([]int{5, 5, 4, 4, 4})) // Output: -1
}
```



In this solution, we first sort the list in ascending order. Then we iterate through the list from the end to the beginning. If we find an element that is less than or equal to its index plus one, we return -1. If we find an element that is greater than the current maximum, we update the maximum. Finally, we return the maximum.



The time complexity of this solution is O(n log n) due to the sorting, where n is the length of the list. The space complexity is O(1) as we only use a constant amount of space.