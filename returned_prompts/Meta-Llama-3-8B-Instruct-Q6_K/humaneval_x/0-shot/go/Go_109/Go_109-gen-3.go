Here is a solution in Go:

```go
import (
    "math"
    "sort"
)

func MoveOneBall(arr []int) bool {
    if len(arr) == 0 {
        return true
    }
    sort.Ints(arr)
    last := arr[0]
    for i := 1; i < len(arr); i++ {
        if arr[i] < last {
            return false
        }
        last = arr[i]
    }
    return true
}
```

Explanation:
This function first checks if the input array is empty. If it is, the function returns true because an empty array is considered sorted. Then, it sorts the array. After sorting, it iterates over the array, checking if the current element is less than the previous one. If it finds such an element, it means that the array cannot be sorted by performing right shift operations, so the function returns false. If the function finishes iterating over the array without finding any elements that are less than the previous one, it means that the array can be sorted by performing right shift operations, so the function returns true.