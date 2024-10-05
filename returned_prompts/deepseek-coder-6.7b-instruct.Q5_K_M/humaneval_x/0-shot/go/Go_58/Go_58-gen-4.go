In your code, you are correct in using sort.Ints() to sort both lists. However, you are using the function sort.SearchInts() incorrectly. sort.SearchInts() is used to search for a specific element in a sorted slice. It returns the index of the element if found, or the index where the element could be inserted to maintain the sorted order.

You should use a map to store the elements of the first list and then check if the elements of the second list are in the map. This is more efficient and more readable.

Here is the corrected code:

```go
import (
    "sort"
)

// Return sorted unique Common elements for two lists.
// 
// >>> Common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
// [1, 5, 653]
// 
// >>> Common([5, 3, 2, 8], [3, 2])
// [2, 3]
func Common(l1 []int, l2 []int) []int {
    sort.Ints(l1)
    sort.Ints(l2)

    m := make(map[int]bool)
    for _, v := range l1 {
        m[v] = true
    }

    res := []int{}
    for _, v := range l2 {
        if m[v] {
            res = append(res, v)
            delete(m, v)
        }
    }

    sort.Ints(res)
    return res
}
```

In this code, we use a