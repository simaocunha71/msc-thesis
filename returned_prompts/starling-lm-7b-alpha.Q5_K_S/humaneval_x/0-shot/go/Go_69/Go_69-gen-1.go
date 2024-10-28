
```go
package main

import (
	"fmt"
	"sort"
)

func Search(lst []int) int {
	if len(lst) == 0 {
		return -1
	}
	sort.Slice(lst, func(i, j int) bool {
		return lst[i] < lst[j]
	})
	for i := range lst {
		if lst[i] > i {
			break
		}
	}
	return lst[i]
}

func main() {
	fmt.Println(Search([]int{4, 1, 2, 2, 3, 1}))
	fmt.Println(Search([]int{1, 2, 2, 3, 3, 3, 4, 4, 4}))
	fmt.Println(Search([]int{5, 5, 4, 4, 4}))
}
```

In this problem, we need to find the greatest integer that is greater than zero and has a frequency greater than or equal to the value of the integer itself. To solve this problem, we can sort the list of integers in ascending order. Then, we iterate through the sorted list and check if the current integer is greater than its index. If it is, we break the loop and return the current integer, as it satisfies the condition. If not, we continue to the next integer. If no such integer is found, we return -1.

The code provided demonstrates the solution. The `Search` function takes a slice of integers as input and returns the greatest integer that satisfies the condition. The `sort.Slice` function is used to sort the list in ascending order. The `for` loop iterates through the sorted list and checks if the current integer is greater than its index. If it is, the loop is broken and the function returns the current integer. If not, the loop continues to the next integer. If no such integer is found, the function returns -1.

In the `main` function, the `Search` function is called with different test cases to demonstrate its usage. The results are printed to the console using `fmt.Println`.
```

```python

``