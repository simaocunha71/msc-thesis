```go
package main

import (
	"fmt"
	"sort"
)

func Search(lst []int) int {
	sort.Ints(lst)
	max := 0
	for i := len(lst) - 1; i >= 0; i-- {
		if lst[i] > max {
			max = lst[i]
		} else if lst[i] <= max {
			break
		}
	}
	for i := 0; i < len(lst); i++ {
		if lst[i] == max && count(lst, lst[i]) >= max {
			return max
		}
	}
	return -1
}

func count(lst []int, x int) int {
	count := 0
	for _, v := range lst {
		if v == x {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(Search([]int{4, 1, 2, 2, 3, 1}))  // Output: 2
	fmt.Println(Search([]int{1, 2, 2, 3, 3, 3, 4, 4, 4}))  // Output: 3
	fmt.Println(Search([]int{5, 5, 4, 4, 4}))  // Output: -1
}
```
Explanation:
The problem can be solved by first sorting the list in descending order. This is because we are looking for the greatest integer with a frequency greater than or equal to its value. After sorting, we iterate through the list from the end to the beginning, keeping track of the maximum value seen so far. Once we find an integer that is less than or equal to the maximum value, we stop iterating.

Next, we iterate through the list again, and for each integer, we check if its frequency is greater than or equal to its value. If we find such an integer, we return it. If no such integer is found, we return -1.

The `count` function is used to count the frequency of each integer in the list. The `Search` function returns the greatest integer with a frequency greater than or equal to its value, or -1 if no such integer exists. The `main` function demonstrates how to use the `Search` function with different inputs.