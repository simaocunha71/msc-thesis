Here is a possible solution in Go:

```go
package main

import (
	"sort"
)

func SortedListSum(lst []string) []string {
	// Delete strings with odd lengths
	for i := 0; i < len(lst); i++ {
		if len(lst[i])%2 == 1 {
			lst = append(lst[:i], lst[i+1:]...)
			i--
		}
	}

	// Sort by length and alphabetically
	sort.Slice(lst, func(i, j int) bool {
		if len(lst[i]) == len(lst[j]) {
			return lst[i] < lst[j]
		}
		return len(lst[i]) < len(lst[j])
	})

	return lst
}

func main() {
	list := []string{"aa", "a", "aaa"}
	result := SortedListSum(list)
	fmt.Println(result) // Output: ["aa"]
}
```

This function works by first deleting the strings with odd lengths using the `append` function. Then it sorts the list by length and alphabetically using the `sort.Slice` function. Finally, it returns the sorted list.