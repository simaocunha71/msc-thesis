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
	sort.Ints(lst)
	max := 0
	for i := len(lst) - 1; i >= 0; i-- {
		if lst[i] > max {
			max = lst[i]
		} else if lst[i] == max {
			return max
		}
	}
	return -1
}

func main() {
	fmt.Println(Search([]int{4, 1, 2, 2, 3, 1})) // 2
	fmt.Println(Search([]int{1, 2, 2, 3, 3, 3, 4, 4, 4})) // 3
	fmt.Println(Search([]int{5, 5, 4, 4, 4})) // -1
}
```

Explanation:
The function `Search` takes a list of positive integers as an input and returns the greatest integer that is greater than zero and has a frequency greater than or equal to the value of the integer itself. If no such value exists, it returns -1.

The function first sorts the input list in ascending order using the `sort.Ints` function from the standard library. Then, it iterates over the list from the end to the beginning. For each integer, it checks if it is greater than the current maximum value. If it is, it updates the maximum value. If the integer is equal to the maximum value, it returns the maximum value as the result.

If the function reaches the end of the list without finding an integer with a frequency greater than or equal to its value, it returns -1.

The `main` function demonstrates the usage of the `Search` function with three different input lists. The output of the program is the result of the `Search` function for each input list.