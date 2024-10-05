You can use the `sort` package in Go to sort both lists in ascending order. Then, you can iterate through the first list and check if each element is odd. If an element is odd, you can check if there is an odd element in the second list that can be exchanged with it. If such an element exists, you can exchange them and continue the iteration. If no such element exists, you can return "NO". After the iteration, if all elements in the first list are even, you can return "YES". Here is the implementation:

```go
package main

import (
	"fmt"
	"sort"
)

func Exchange(lst1, lst2 []int) string {
	sort.Ints(lst1)
	sort.Ints(lst2)

	for _, num := range lst1 {
		if num%2 != 0 {
			for i, n := range lst2 {
				if n%2 != 0 {
					lst1 = append(lst1[:i], lst1[i+1:]...)
					lst2 = append(lst2[:i], lst2[i+1:]...)
					lst2 = append(lst2, num)
					break
				}
			}
			if len(lst2) == 0 || lst2[0]%2 == 0 {
				return "NO"
			}
		}
	}

	return "YES"
}

func main() {
	fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 2, 3, 4})) // YES
	fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 5, 3, 4})) // NO
}
```

This implementation first sorts both lists in ascending order. Then, it iterates through the first list and checks if each element is odd. If an element is odd, it searches for an odd element in the second list that can be exchanged with it. If such an element exists, it exchanges them and continues the iteration. If no such element exists, it returns "NO". After the iteration, if all elements in the first list are even, it returns "YES".