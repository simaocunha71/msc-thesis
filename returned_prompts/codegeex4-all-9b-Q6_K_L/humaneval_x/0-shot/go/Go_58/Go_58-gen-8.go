```go
import (
    "sort"
)

// Return sorted unique Common elements for two lists.
// >>> Common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
// [1, 5, 653]
// >>> Common([5, 3, 2, 8], [3, 2])
// [2, 3]
func Common(l1 []int,l2 []int) []int {
    sort.Ints(l1)
    sort.Ints(l2)
    i, j := 0, 0
    result := make([]int, 0)
    for i < len(l1) && j < len(l2) {
        if l1[i] == l2[j] {
            if len(result) == 0 || result[len(result)-1] != l1[i] {
                result = append(result, l1[i])
            }
            i++
            j++
        } else if l1[i] < l2[j] {
            i++
        } else {
            j++
        }
    }
    return result
}
```
