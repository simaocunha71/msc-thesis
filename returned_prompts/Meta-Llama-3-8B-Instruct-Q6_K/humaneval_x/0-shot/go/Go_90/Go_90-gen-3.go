Here is a Go function that solves the problem:

```go
import (
    "math"
    "sort"
)

func NextSmallest(lst []int) interface{} {
    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)
    for i := 1; i < len(lst); i++ {
        if lst[i] > lst[0] {
            return lst[i]
        }
    }
    return nil
}
```

This function first checks if the list has less than 2 elements. If so, it returns nil. Otherwise, it sorts the list in ascending order. Then it iterates over the list from the second element to the end. If it finds an element that is greater than the first element, it returns that element. If it doesn't find such an element, it returns nil. 

For example, `NextSmallest([1, 2, 3, 4, 5])` returns 2, `NextSmallest([5, 1, 4, 3, 2])` returns 2, `NextSmallest([])` returns nil, and `NextSmallest([1, 1])` returns nil. 