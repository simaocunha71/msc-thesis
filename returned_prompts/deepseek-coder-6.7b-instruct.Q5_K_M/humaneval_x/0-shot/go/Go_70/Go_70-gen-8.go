    if len(lst) == 0 {
        return []int{}
    }

    sort.Ints(lst)
    res := make([]int, len(lst))
    for i := 0; i < len(lst)/2; i++ {
        res[i*2] = lst[i]
        res[i*2+1] = lst[len(lst)-i-1]
    }
    if len(lst)%2 != 0 {
        res[len(lst)-1] = lst[len(lst)/2]
    }
    return res
}
```

This solution works by first sorting the list in increasing order. Then we create a new list where we fill in the smallest and largest values from the original list, then the next smallest and largest and so on. If the length of the original list is odd, we append the middle element to the result list at the end.

This solution has a time complexity of O(n log n) due to the sorting operation, and a space complexity of O(n) for the result list.

Test cases:

```go
func main() {
    fmt.Println(StrangeSortList([]int{1, 2, 3, 4})) // [1, 4, 2, 3]
    fmt.Println(StrangeSortList([]int{5, 5, 5, 5})) // [5, 5, 5, 5]
    fmt.Println(StrangeSortList([]int{}))            // []
}
```

This code will print:

```
[1 4 2 3]
[5 5 5 5]
[]
```

Which are the correct results.
*/

package main

import (
	"fmt"
	"sort"
)

func StrangeSortList(lst []int) []int {
	if len(lst) == 0 {
		return []int{}
	}

	sort.Ints(lst)
	res := make([]int, len(lst))
	for i := 0; i < len(lst)/2; i++