Here is the solution in Go:

```go
import (
    "sort"
)

func StrangeSortList(lst []int) []int {
    sorted := make([]int, len(lst))
    copy(sorted, lst)
    sort.Slice(sorted, func(i, j int) bool {
        return sorted[i] < sorted[j]
    })

    result := make([]int, len(lst))
    for i := 0; i < len(lst); i++ {
        if i%2 == 0 {
            result[i] = sorted[i/2]
        } else {
            result[i] = sorted[len(lst)-i/2-1]
        }
    }
    return result
}
```
In this solution, we first sort the list in ascending order. Then we create a new list and fill it with elements from the sorted list in a strange order. If the index of the element is even, we take the element from the middle of the sorted list. If the index is odd, we take the element from the end of the sorted list.